#!/usr/bin/env python


class LocalData:
	""" Data class containing data structures and methods to interact with them """

	# 'session_id'
	session_id = str()

	# ('ipv4', 'ipv6', 'port')
	tracker = tuple()

	# (file_md5, filename)
	shared_files = list()

	# [('ipv4_i', 'ipv6_i', 'port_i', 'part_list_i')]
	part_list_table = list()

	# bytearray
	downloading_part_list = bytearray()

	# number of parts owned
	num_parts_owned = int()

	# tracker management ------------------------------------------------------------
	@classmethod
	def get_tracker(cls) -> tuple:
		return cls.tracker

	@classmethod
	def set_tracker(cls, tracker: tuple) -> None:
		cls.tracker = tracker

	@classmethod
	def clear_tracker(cls) -> None:
		cls.tracker = tuple()

	@classmethod
	def tracker_is_empty(cls) -> bool:
		if not cls.tracker:
			return True
		else:
			return False

	@classmethod
	def get_tracker_ip4(cls) -> str:
		return cls.tracker[0]

	@classmethod
	def get_tracker_ip6(cls) -> str:
		return cls.tracker[1]

	@classmethod
	def get_tracker_port(cls) -> int:
		return cls.tracker[2]
	# ----------------------------------------------------------------------------------
	
	# session_id management ------------------------------------------------------------
	@classmethod
	def set_session_id(cls, session_id: str) -> None:
		cls.session_id = session_id

	@classmethod
	def get_session_id(cls) -> str:
		return cls.session_id
	# ---------------------------------------------------------------------------------

	# shared_file management ------------------------------------------------------------
	@classmethod
	def add_shared_file(cls, file_md5: str, filename: str) -> None:
		cls.shared_files.append((file_md5, filename))

	@classmethod
	def is_shared_file(cls, file_md5: str, filename: str) -> bool:
		if (file_md5, filename) in cls.shared_files:
			return True
		return False

	@classmethod
	def get_shared_files(cls) -> list:
		return cls.shared_files

	@classmethod
	def get_shared_file_md5(cls, file: tuple) -> str:
		return file[0]

	@classmethod
	def get_shared_file_name(cls, file: tuple) -> str:
		return file[1]

	@classmethod
	def get_shared_file_name_from_md5(cls, file_md5: str) -> str:
		shared_files = cls.get_shared_files()
		for file in shared_files:
			if cls.get_shared_file_md5(file) == file_md5:
				return cls.get_shared_file_name(file)

	@classmethod
	def clear_shared_files(cls) -> None:
		cls.shared_files.clear()
	# ---------------------------------------------------------------------------------

	# downloadables_file management ---------------------------------------------------
	@classmethod
	def get_downloadable_file_md5(cls, file: tuple) -> str:
		return file[0]

	@classmethod
	def get_downloadable_file_name(cls, file: tuple) -> str:
		return file[1]

	@classmethod
	def get_downloadable_file_length(cls, file: tuple) -> int:
		return int(file[2])

	@classmethod
	def get_downloadable_file_part_length(cls, file: tuple) -> int:
		return int(file[3])
	# ---------------------------------------------------------------------------------

	# part list table management ------------------------------------------------------
	@classmethod
	def set_part_list_table(cls, part_list_table: list) -> None:
		cls.part_list_table = part_list_table

	@classmethod
	def get_part_list_table(cls) -> list:
		return cls.part_list_table

	# ---------------------------------------------------------------------------------

	# downloading part list -----------------------------------------------------------

	@classmethod
	def set_downloading_part_list(cls, part_list_length) -> None:
		cls.downloading_part_list = bytearray(part_list_length)

	# ---------------------------------------------------------------------------------

	# downloading part list -----------------------------------------------------------
	@classmethod
	def set_num_parts_owned(cls, num_parts_owned: int) -> None:
		cls.num_parts_owned = num_parts_owned

	@classmethod
	def get_num_parts_owned(cls) -> None:
		return cls.num_parts_owned
	# ---------------------------------------------------------------------------------
