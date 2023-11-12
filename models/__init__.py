#!/usr/bin/python3
"""Init file for package"""
import engine.file_storage

storage = engine.file_storage.FileStorage()
storage.reload()
