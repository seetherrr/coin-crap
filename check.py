import pandas as pd
from functools import partial
import colorama
import sys, math

filenames = sys.argv[1:]

if len(filenames) == 0:
  print('please specify some CSVs')
  raise SystemExit

def red_print(s):
  print('%s%s%s' % (colorama.Fore.RED, s, colorama.Fore.RESET))

def maybe_red_print(s, b):
  print('%s%s%s' % (
    '' if b else colorama.Fore.RED,
    s,
    '' if b else colorama.Fore.RESET
  ))

def is_growing(series):
  x = -math.inf
  for n in series:
    if x >= n:
      return False
  return True

def is_interval(xs, interval):
  result = True
  last_x = xs[0]
  for row_index, x in enumerate(xs[1:]):
    expected_value = last_x + interval
    if expected_value != x:
      red_print('expected #%d to have value %d but it had %d instead' % (row_index, expected_value, x))
      result = False
    last_x = x
  return result

def series_is_float_str(xs):
  result = True
  for row_index, x in enumerate(xs):
    try:
      float(x)
    except ValueError:
      red_print('series contains non-floatish string "%s" at row %d' % (x, row_index))
      result = False
  return result

def handle_filename(filename):
  result = True
  candles_df = pd.read_csv(filename)
  # check if Timestamp column is growing
  timestamp_series = candles_df['Timestamp']

  success = is_growing(timestamp_series)
  maybe_red_print('timestamp series is%s growing' % ('' if success else ' not'), success)
  if not success: result = False

  success = is_interval(timestamp_series, 60)
  maybe_red_print('timestamp series is%s on an interval of 60 seconds' % ('' if success else ' not'), success)
  if not success: result = False

  for column in ['Open', 'High', 'Low', 'Close', 'Volume_(BTC)', 'Volume_(Currency)', 'Weighted_Price']:
    success = series_is_float_str(candles_df[column])
    maybe_red_print('%s series is%s 100%% floatish strings' % (column, '' if success else ' not'), success)
    if not success: result = False

  return success

for filename in filenames:
  success = handle_filename(filename)
  maybe_red_print('%s: %s' % (filename, 'passed all tests' if success else 'failed some test(s)'), success)
  print()
