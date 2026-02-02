from nicegui import ui
from typing import List, Dict
from datetime import datetime


class UpdateWorkflow:
    """Update workflow panel component"""
    
    def __init__(self):
        """Initialize update workflow component"""
        self.log_messages: List[str] = []
        self.has_error = False
        self.error_message = ""
        
        # UI elements
        self.log_container = None
        self.alert_container = None
    
    def render(self):
        """Render the update workflow panel"""
        with ui.column().classes('sidebar-right workflow-container'):
            # Workflow title
            ui.label('Activity Log').classes('workflow-title')
            
            # Log section
            with ui.column().classes('workflow-section'):
                self.log_container = ui.column().classes('activity-log')
                self.add_log('Waiting for update to start...')
            
            # Alert container (initially hidden)
            self.alert_container = ui.column().classes('hidden')
    
    def start_update(self, device_name: str, firmware_version: str):
        """
        Start an update workflow
        
        Args:
            device_name: Name of device being updated
            firmware_version: Firmware version being installed
        """
        self.has_error = False
        self.log_messages = []
        
        self.add_log(f'Starting firmware update for {device_name}')
        self.add_log(f'Target firmware version: {firmware_version}')
    
    def add_log(self, message: str):
        """
        Add a log message
        
        Args:
            message: Log message text
        """
        timestamp = datetime.now().strftime('%H:%M:%S')
        log_entry = f'[{timestamp}] {message}'
        self.log_messages.append(log_entry)
        
        # Update UI
        if self.log_container:
            with self.log_container:
                ui.label(log_entry).classes('text-xs')
    
    def show_error(self, error_message: str):
        """
        Show an error dialog
        
        Args:
            error_message: Error message text
        """
        self.has_error = True
        self.error_message = error_message
        
        with ui.dialog() as dialog, ui.card().classes('w-96'):
            ui.label('Firmware Update Error').classes('text-h6 text-negative')
            ui.label(error_message).classes('text-sm mt-2')
            with ui.row().classes('gap-2 mt-4 justify-end w-full'):
                ui.button('Close', on_click=dialog.close).props('flat')
        
        dialog.open()
    
    def show_error_with_force(self, error_message: str):
        """
        Show an error dialog suggesting to enable force upload checkbox
        
        Args:
            error_message: Error message text
            force_checkbox: Reference to the force upload checkbox to enable
        """
        self.has_error = True
        self.error_message = error_message
        
        with ui.dialog() as dialog, ui.card().classes('w-96'):
            ui.label('Firmware Update Failed').classes('text-h6 text-negative')
            ui.label(error_message).classes('text-sm mt-2')
            ui.label('To bypass safety checks, enable the "Force upload" checkbox and try again.').classes('text-sm mt-3 font-semibold text-warning')
            
            
            with ui.row().classes('gap-2 mt-4 justify-end w-full'):
                ui.button('Close', on_click=dialog.close).classes('btn btn-secondary')
        
        dialog.open()
    
    def hide_error(self):
        """Hide error alert"""
        self.has_error = False
        if self.alert_container:
            self.alert_container.classes(add='hidden')
    
    def on_retry(self):
        """Handle retry button click"""
        self.hide_error()
        self.add_log('Retrying update...')
        ui.notify('Retrying update', type='info')
    
    def on_rollback(self):
        """Handle rollback button click"""
        self.hide_error()
        self.add_log('Rolling back to previous firmware...')
        ui.notify('Rolling back firmware', type='warning')
    
    def complete_update(self, success: bool):
        """
        Complete the update workflow
        
        Args:
            success: Whether update completed successfully
        """
        if success:
            self.add_log('✓ Firmware update completed successfully!')
            ui.notify('Firmware update completed!', type='positive')
        else:
            self.show_error('Firmware update failed. Please check the logs and try again.')