import functools
from flask import jsonify, render_template
import logging

# Endpoint decorator
# Try/Except and return JSON
def endpoint(func):
	@functools.wraps(func)
	def wrapper(*args, **kwargs):
		try:
			return jsonify(func(*args, **kwargs))
		except Exception as e:
			logging.error(f"Error when calling endpoint '{func.__name__}': {e}")
			return jsonify({ 'error': 'Something went wrong' })
	
	return wrapper


# Page decorator
# Try/Except and show error.html on error
def page(func):
	@functools.wraps(func)
	def wrapper(*args, **kwargs):
		try:
			return func(*args, **kwargs)
		except Exception as e:
			logging.error(f"Error when loading page '{func.__name__}': {e}")
			return render_template('error.html')
	
	return wrapper
