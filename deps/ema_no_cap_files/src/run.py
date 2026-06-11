import os
import time

datasets = ['amazon_books_60core']
models = ['BPR', 'DMF', 'LINE', 'MultiDAE', 'NGCF', 'DGCF', 'LightGCN', 'CKE', 'CFKG', 'KGCN', 'KGNNLS']


tolerance_step  = 10
smoothing_factor = 2/(tolerance_step+1)

for dataset in datasets:
    for model in models:
        os.system(f"python src/tracker_ema_no_cap.py --dataset={dataset} --model={model} --tolerance_step={tolerance_step} --smoothing_factor={smoothing_factor}")
        time.sleep(30)