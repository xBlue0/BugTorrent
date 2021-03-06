#!/usr/bin/env python

import sqlite3
from sqlite3 import Error
import os.path


def exist(db_filename: str) -> bool:
	""" Check if the given db exist
	:param db_filename: the db filename
	:return: bool - True or False either if exists or not
	"""
	if os.path.exists(db_filename):
		return True
	return False


def create_database(db_filename: str) -> None:
	""" Create a sqlite db file with the structure defined in the 'schema.sql' file
	:param: db_filename: the db filename
	"""
	try:
		db_file = open(db_filename, "w+")
		sqlscript = open('tracker/database/schema.sql', 'r')
	except IOError as e:
		print(e)
		exit(0)

	if db_file is not None and sqlscript is not None:
		# create a database connection
		conn = get_connection(db_filename)

		try:
			# create files table
			conn.executescript(sqlscript.read())
			# commits the statements
			conn.commit()
			# close the database
			conn.close()
		except Error as e:
			conn.rollback()
			conn.close()
			print(e)
			exit(0)

	else:
		print("Error: cannot create the database file.")


def reset_database(db_filename: str) -> bool:
	""" Refresh the tables of the database
	:param db_filename: the db filename
	:return bool - True or False either if succeeds or fails
	"""
	try:
		sqlscript = open('tracker/database/reset.sql', 'r')
	except IOError as e:
		print(e)
		exit(0)
	# create a database connection
	conn = get_connection(db_filename)

	try:
		# delete all tables content
		conn.executescript(sqlscript.read())
		# commits the statement
		conn.commit()
		# close the database
		conn.close()
		return True
	except Error as e:
		conn.rollback()
		conn.close()
		print(e)
		exit(0)
		return False


def fill_seeds(db_filename: str) -> bool:
	""" Refresh the tables of the database
	:param db_filename: the db filename
	:return bool - True or False either if succeeds or fails
	"""
	try:
		reset_script = open('tracker/database/reset.sql', 'r')
		seeds_script = open('tracker/database/seeds.sql', 'r')
	except IOError as e:
		print(e)
		exit(0)
	# create a database connection
	conn = get_connection(db_filename)

	try:
		conn.executescript(reset_script.read())
		conn.executescript(seeds_script.read())
		# commits the statement
		conn.commit()
		# close the database
		conn.close()
		return True
	except Error as e:
		conn.rollback()
		conn.close()
		print(e)
		exit(0)
		return False


def get_connection(db_filename: str) -> sqlite3.Connection:
	""" Create a database connection to the given SQLite database
	:param db_filename: the db filename
	:return Connection - Connection object or None
	"""
	try:
		return sqlite3.connect(db_filename)

	except Error as e:
		raise e
