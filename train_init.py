from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import logging

from rasa_core.agent import Agent
from rasa_core import config as policy_config
from rasa_core.policies import FallbackPolicy, KerasPolicy, MemoizationPolicy

if __name__ == '__main__':
	logging.basicConfig(level='INFO')
	
	training_data_file = './data/stories.md'
	model_path = './models/dialogue'

   ## fallback = FallbackPolicy(fallback_action_name="utter_unclear", core_threshold=0.2, nlu_threshold=0.1)
	
    ##policies = policy_config.load('policies.yml')
	agent = Agent('weather_domain.yml', policies = [MemoizationPolicy(), KerasPolicy()])
	
	agent.train(training_data_file)
			
	agent.persist(model_path)