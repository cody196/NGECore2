import sys

def setup(core, actor, buff):
	return
	
def run(core, actor, target, commandString):
	if target is None:
		target = actor
	core.buffService.addGroupBuff(target, 'of_buff_def_4', actor)
	return
	