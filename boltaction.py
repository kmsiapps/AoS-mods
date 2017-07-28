"""
Original script "WeaponDisable" by thepolm3
Edited by kmsi(kmsiapps@gmail.com)
Boltaction.py : Version 3(2017.02.07)
- One ammo, One clip. + Rifle Only
- Now works well on 0.75B(2017.01.17)
- Now reducing ammo behavior works correctly(2017.02.07)
"""
from pyspades.server import weapon_reload
from pyspades.constants import *

def apply_script(protocol,connection,config):
    class kmsiConnection(connection):
               
        def on_spawn(self, pos):
            self.set_ammo(1,50)
            return connection.on_spawn(self, pos)

        def on_spawn(self, pos):
            self.set_ammo(1,50)
            if not self.weapon==RIFLE_WEAPON :
                self.send_chat('%% RIFLE Only.')
                self.set_weapon(RIFLE_WEAPON)
                self.kill(type = CLASS_CHANGE_KILL)
                return connection.on_spawn(self, pos)
            
        def on_weapon_set(self, value):
            if value==2:
                self.send_chat('%% RIFLE Only.')
                return False
            if value==1:
                self.send_chat('%% RIFLE Only.')
                return False
            return connection.on_weapon_set(self, value)
            
        def _on_reload(self):
            weapon_reload.player_id = self.player_id
            weapon_reload.clip_ammo = self.weapon_object.current_ammo
            weapon_reload.reserve_ammo = self.weapon_object.current_stock
            self.send_contained(weapon_reload)
            if not (self.weapon_object.current_ammo<1):
                self.set_ammo(1,self.weapon_object.current_ammo+self.weapon_object.current_stock-1)
            
        def set_ammo(self, new_ammo, new_stock=None):
            new_ammo=max(min(255,new_ammo),0)
            new_stock=max(min(255,new_stock),0)
            weapon=self.weapon_object
            weapon.current_ammo = new_ammo
            weapon_reload.player_id = self.player_id
            weapon_reload.clip_ammo = new_ammo
            weapon.current_stock = new_stock
            weapon_reload.reserve_ammo = new_stock
            self.send_contained(weapon_reload)
                
    return protocol,kmsiConnection
