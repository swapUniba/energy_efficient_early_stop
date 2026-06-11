"""
The collection of global configurations
"""
CONFIG = {

	'MODELS':				['BPR', 'CFKG', 'CKE', 'DMF', 'KGCN', 'KGNNLS', 'LINE', 'MultiDAE', 'LightGCN', 'NGCF', 'DGCF'],
	'LOG_FILE':				'log/carbon_tuning.log',
	'LOG_FILE_DEFAULT':		'log/carbon_default.log',
	'DATASET_PATH':			'data/',
	'RESULT_PATH':			'results/',
	'RESULT_PATH2':			'results_default_es/',
	'EXPERIMENT_RESULTS':	'exp_paper/',
	'EMISSIONS_FILE':		'/emissions.csv',
	'GRAPH_PATH':			'graphs/',
	'METRICS_FILE':			'/metrics.csv',
	'PARAMS_FILE':			'/params.csv',
	'STATIC_CONFIG_FILE':	'src/config/_params.yaml',
	'HP_CONFIG_PATH':		'src/config/hyperparam/',
	'COUNTER':				1,
	'DATASETAZURE_FILE':	'notebooks/data/dataset_azure.csv',
	'DATASET_FILE':			'notebooks/data/dataset.csv'
}


def get_global_config():
	"""
	The getter method
	"""
	return CONFIG


def set_global_config(key, value):
	"""
	The setter method
	"""
	CONFIG.update({key: value})