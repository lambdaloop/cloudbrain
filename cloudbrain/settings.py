# Metric metadata of all wearable devices accepted by CloudBrain.
# The format is the following:
# 
# DEVICE_METADATA = 
# [
#   {
#   'device_name': <string>,
#    'device_type': <'eeg_headset' | 'heart_rate_monitor'>,
#    'metrics': 
#      [
#        {
#            'metric_name': <string>,
#            'num_channels': <int>,
#            'metrics_description' : <string>
#         },
#            ...
#            ...
#        {
#            'metric_name': <string>,
#            'num_channels': <int>,
#            'metrics_description' : <string>
#         }
#      ]
#   }
#      ...
#      ...
#   {
#    'device_name': <string>,
#    'device_type': <'eeg_headset' | 'heart_rate_monitor'>,
#    'metrics': 
#      [
#        {
#            'metric_name': <string>,
#            'num_channels': <int>,
#            'metrics_description' : <string>
#         },
#            ...
#            ...
#        {
#            'metric_name': <string>,
#            'num_channels': <int>,
#            'metrics_description' : <string>
#         }
#      ]
#   }
# ]

DEVICE_METADATA = [
  {'device_name': 'openbci',
   'device_type': 'eeg_headset',
   'metrics':
     [
       {
         'metric_name': 'eeg',
         'num_channels': 8,
         'metric_description': 'Raw eeg data coming from the OpenBCI channels'
       }
     ]
  },
  {
    'device_name': 'muse',
    'device_type': 'eeg_headset',
    'metrics':
      [
        {
          'metric_name': 'eeg',
          'num_channels': 4,
          'metric_description': 'Raw eeg data coming from the 4 channels of the Muse'
        },
        {
          'metric_name': 'horseshoe',
          'num_channels': 4,
          'metric_description': 'Status indicator for each channel (1 = good, 2 = ok, >=3 bad)'
        },
        {
          'metric_name': 'concentration',
          'num_channels': 1,
          'metric_description': None
        },
        {
          'metric_name': 'mellow',
          'num_channels': 1,
          'metric_description': None
        },
        {
          'metric_name': 'acc',
          'num_channels': 3,
          'metric_description': None
        },
        {
          'metric_name': 'delta_absolute',
          'num_channels': 4,
          'metric_description': None
        },
        {
          'metric_name': 'theta_absolute',
          'num_channels': 4,
          'metric_description': None
        },
        {
          'metric_name': 'beta_absolute',
          'num_channels': 4,
          'metric_description': None
        },
        {
          'metric_name': 'gamma_absolute',
          'num_channels': 4,
          'metric_description': None
        },
        {
          'metric_name': 'delta_relative',
          'num_channels': 4,
          'metric_description': None
        },
        {
          'metric_name': 'theta_relative',
          'num_channels': 4,
          'metric_description': None
        },
        {
          'metric_name': 'beta_relative',
          'num_channels': 4,
          'metric_description': None
        },
        {
          'metric_name': 'gamma_relative',
          'num_channels': 4,
          'metric_description': None
        },
        {
          'metric_name': 'is_good',
          'num_channels': 4,
          'metric_description': 'Strict data quality indicator for each channel, 0= bad, 1 = good.'
        },
        {
          'metric_name': 'blink',
          'num_channels': 1,
          'metric_description': None
        },
        {
          'metric_name': 'jaw_clench',
          'num_channels': 1,
          'metric_description': None
        },

      ]
  },
  {
    'device_name': 'neurosky',
    'device_type': 'eeg_headset',
    'metrics': [
      {
        'metric_name': 'concentration',
        'num_channels': 1,
        'metric_description': None
      },
      {
        'metric_name': 'meditation',
        'num_channels': 1,
        'metric_description': None
      },
      {
        'metric_name': 'signal_strength',
        'num_channels': 1,
        'metric_description': None
      },
    ]
  },
  {
    'device_name': 'pulsesensor',
    'device_type': 'heart_rate_monitor',
    'metrics': [
      {
        'metric_name': 'raw',
        'num_channels': 1,
        'metric_description': None
      }
    ]
  }
]
