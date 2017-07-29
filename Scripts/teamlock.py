"""
Script by kmsi(kmsiapps@gmail.com)
When someone logins, switch his team to spectator_team.
Usage : /teamlock
"""
from commands import add, admin

lock_team=False

@admin
def teamlock(connection):
	global lock_team
	if lock_team==True:
		lock_team=False
	elif lock_team==False:
		lock_team=True
	value=lock_team
	on_off = ['UNLOCKED', 'LOCKED'][int(value)]
	connection.protocol.send_chat('BOTH TEAM are %s' % on_off)
add(teamlock)
		
def apply_script(protocol, connection, config):
	class kmsiconnection(connection):
		def on_login(self, name):
			if lock_team:
				self.send_chat('Both team are locked. You only can spectate!')
				self.set_team(self.protocol.spectator_team)
				self.respawn()
			return connection.on_login(self, name)
	return protocol, kmsiconnection	