#!/usr/bin/python3
"""Init file for the models package"""
import models.engine.file_storage

storage = models.engine.file_storage.FileStorage()
storage.reload()
