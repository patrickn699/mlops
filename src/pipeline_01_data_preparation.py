import os
import yaml
import logging
import argparse

def read_params(config_file):
    with open(config_file) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config


def main(config_file,datasource):
    config = read_params(config_file)
    print(config)



if __name__ == '__main__':
    args = argparse.ArgumentParser()
    default_config_path = os.path.join('config','parameters.yaml')
    args.add_argument('--config',default=default_config_path)
    args.add_argument('--datasource',default=None)

    passed_args = args.parse_args()
    
    main(config_file=passed_args.config,datasource = passed_args.datasource)
    
