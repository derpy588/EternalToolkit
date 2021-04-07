import importlib
import os

Active_Features = []

for subdir, dirs, files in os.walk('./Features'):
    if not subdir == './Features\__pycache__':
        for file in files:
            if not file == 'base.py' and not file == '__init__.py' and not file == 'FeaturesRegister.py':
                print("Enabling Feature "+file.replace('.py', ''))
                feature = importlib.import_module('Features.'+file.replace('.py', ''))
                Active_Features.append(feature.Feature())