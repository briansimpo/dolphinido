
# The number of fingerprints to generate on any given audio samples
FINGERPRINT_LIMIT =  None

# This is used as connectivity parameter for scipy.generate_binary_structure function. This parameter
# changes the morphology mask when looking for maximum peaks on the spectrogram matrix.
# Possible values are: [1, 2]
# Where 1 sets a diamond morphology which implies that diagonal elements are not considered as neighbors (this
# is the value used in the original dejavu code).
# And 2 sets a square mask, i.e. all elements are considered neighbors.
CONNECTIVITY_MASK = 2

# Sampling rate, related to the Nyquist conditions, which affects
# the range frequencies we can detect.
DEFAULT_FS = 44100

# Size of the FFT window, affects frequency granularity
DEFAULT_WINDOW_SIZE = 4096

# Ratio by which each sequential window overlaps the last and the
# next window. Higher overlap will allow a higher granularity of offset
# matching, but potentially more fingerprints.
DEFAULT_OVERLAP_RATIO = 0.5

# Degree to which a fingerprint can be paired with its neighbors. Higher values will
# cause more fingerprints, but potentially better accuracy.
DEFAULT_FAN_VALUE = 5  # 15 was the original value.

# Minimum amplitude in spectrogram in order to be considered a peak.
# This can be raised to reduce number of fingerprints, but can negatively
# affect accuracy.
DEFAULT_AMP_MIN = 10

# Number of cells around an amplitude peak in the spectrogram in order
# for Dejavu to consider it a spectral peak. Higher values mean less
# fingerprints and faster matching, but can potentially affect accuracy.
PEAK_NEIGHBORHOOD_SIZE = 10  # 20 was the original value.

# Thresholds on how close or far fingerprints can be in time in order
# to be paired as a fingerprint. If your max is too low, higher values of
# DEFAULT_FAN_VALUE may not perform as expected.
MIN_HASH_TIME_DELTA = 0
MAX_HASH_TIME_DELTA = 200

# If True, will sort peaks temporally for fingerprinting;
# not sorting will cut down number of fingerprints, but potentially
# affect performance.
PEAK_SORT = True

# Number of bits to grab from the front of the SHA1 hash in the
# fingerprint calculation. The more you grab, the more memory storage,
# with potentially lesser collisions of matches.
FINGERPRINT_REDUCTION = 20

# Number of results being returned for file recognition
TOPN = 2

# Peak frequency value
IDX_FREQ_I = 0

# Peak time offset
IDX_TIME_J = 1