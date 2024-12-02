from enum import Enum
from datetime import datetime, timedelta
from typing import List, Optional
import uuid
import json
import os

class TaskStatus(Enum):
    """
    Represents the possible states of a task in our system.
    This allows for clear, type-safe status tracking.
    """
    TODO = "Todo"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    ARCHIVED = "Archived"

class Priority(Enum):
    """
    Defines task priority levels to help users organize and prioritize work.
    """
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    URGENT = "Urgent"

class Tag:
    """
    Represents a tag that can be attached to tasks for categorization.
    """
    def __init__(self, name: str, color: str = "blue"):
        self.id = str(uuid.uuid4())
        self.name = name
        self.color = color

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "color": self.color
        }

class Task:
    """
    Core class representing a single task in our system.
    Encapsulates all properties and behaviors of a task.
    """
    def __init__(
        self, 
        title: str, 
        description: str = "", 
        status: TaskStatus = TaskStatus.TODO,
        priority: Priority = Priority.MEDIUM,
        due_date: Optional[datetime] = None,
        tags: Optional[List[Tag]] = None
    ):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.due_date = due_date
        self.tags = tags or []
        self.subtasks: List[Task] = []
        
    def update_status(self, new_status: TaskStatus):
        """
        Update the status of the task and track when it was last modified.
        """
        self.status = new_status
        self.updated_at = datetime.now()
        
    def add_subtask(self, subtask):
        """
        Add a subtask to this task, creating a hierarchical task structure.
        """
        self.subtasks.append(subtask)
        
    def add_tag(self, tag: Tag):
        """
        Attach a tag to the task for better categorization.
        """
        if tag not in self.tags:
            self.tags.append(tag)
        
    def to_dict(self):
        """
        Serialize the task to a dictionary for easy storage and transfer.
        """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status.value,
            "priority": self.priority.value,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "due_date": self.due_date.isoformat() if self.due_date else None,
            "tags": [tag.to_dict() for tag in self.tags],
            "subtasks": [subtask.to_dict() for subtask in self.subtasks]
        }

class Workspace:
    """
    Represents a workspace that can contain multiple projects.
    Allows for high-level organization of work.
    """
    def __init__(self, name: str):
        self.id = str(uuid.uuid4())
        self.name = name
        self.projects: List[Project] = []
        
    def create_project(self, name: str):
        """
        Create a new project within this workspace.
        """
        project = Project(name, self)
        self.projects.append(project)
        return project

class Project:
    """
    Represents a collection of related tasks.
    Provides a way to group and organize tasks.
    """
    def __init__(self, name: str, workspace: Optional[Workspace] = None):
        self.id = str(uuid.uuid4())
        self.name = name
        self.workspace = workspace
        self.tasks: List[Task] = []
        self.tags: List[Tag] = []
        
    def create_task(
        self, 
        title: str, 
        description: str = "", 
        status: TaskStatus = TaskStatus.TODO,
        priority: Priority = Priority.MEDIUM,
        due_date: Optional[datetime] = None
    ) -> Task:
        """
        Create a new task within this project.
        """
        task = Task(
            title=title, 
            description=description, 
            status=status,
            priority=priority,
            due_date=due_date
        )
        self.tasks.append(task)
        return task
    
    def create_tag(self, name: str, color: str = "blue") -> Tag:
        """
        Create a new tag for this project.
        """
        tag = Tag(name, color)
        self.tags.append(tag)
        return tag
    
    def get_tasks_by_status(self, status: TaskStatus) -> List[Task]:
        """
        Retrieve tasks filtered by their current status.
        """
        return [task for task in self.tasks if task.status == status]
    
    def get_tasks_by_priority(self, priority: Priority) -> List[Task]:
        """
        Retrieve tasks filtered by their priority.
        """
        return [task for task in self.tasks if task.priority == priority]

class TaskManager:
    """
    Central management class that handles persistence and high-level operations.
    """
    def __init__(self, storage_path: str = "task_data"):
        self.workspaces: List[Workspace] = []
        self.storage_path = storage_path
        
        # Ensure storage directory exists
        os.makedirs(storage_path, exist_ok=True)
        
    def create_workspace(self, name: str) -> Workspace:
        """
        Create a new workspace and add it to the task manager.
        """
        workspace = Workspace(name)
        self.workspaces.append(workspace)
        return workspace
    
    def save_to_file(self):
        """
        Serialize and save all workspaces to JSON files.
        """
        for workspace in self.workspaces:
            workspace_file = os.path.join(self.storage_path, f"{workspace.id}.json")
            with open(workspace_file, 'w') as f:
                json.dump({
                    "id": workspace.id,
                    "name": workspace.name,
                    "projects": [
                        {
                            "id": project.id,
                            "name": project.name,
                            "tasks": [task.to_dict() for task in project.tasks],
                            "tags": [tag.to_dict() for tag in project.tags]
                        } for project in workspace.projects
                    ]
                }, f, indent=2)
        
    def load_from_file(self):
        """
        Load workspaces and their data from JSON files.
        Note: This is a simplified version and would need more robust error handling.
        """
        for filename in os.listdir(self.storage_path):
            if filename.endswith('.json'):
                with open(os.path.join(self.storage_path, filename), 'r') as f:
                    data = json.load(f)
                    # Logic to reconstruct workspaces, projects, and tasks would go here
                    # This is a placeholder for a more complete implementation

# Example Usage
def main():
    # Create a task manager
    manager = TaskManager()
    
    # Create a workspace
    personal_workspace = manager.create_workspace("Personal")
    
    # Create a project in the workspace
    learning_project = personal_workspace.create_project("Learning")
    
    # Create some tasks
    python_task = learning_project.create_task(
        "Learn Advanced Python", 
        description="Master OOP and design patterns",
        priority=Priority.HIGH,
        due_date=datetime.now() + timedelta(days=30)
    )
    
    # Add a tag to the task
    coding_tag = learning_project.create_tag("Coding", "blue")
    python_task.add_tag(coding_tag)
    
    # Update task status
    python_task.update_status(TaskStatus.IN_PROGRESS)
    
    # Save the workspace
    manager.save_to_file()

if __name__ == "__main__":
    main()