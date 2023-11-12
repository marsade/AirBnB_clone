#!/usr/bin/python3
"""Init file for package"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
