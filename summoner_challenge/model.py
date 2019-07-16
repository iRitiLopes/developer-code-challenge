import pandas as pd

def atk_speed():
    data = pd.read_csv(r'files/dataset_1.csv')
    return data

def atk_damage():
    data = pd.read_csv(r'files/dataset_2.csv')
    return data

def atk_dps():
    speed = atk_speed()
    damage = atk_damage()

    dps = pd.merge(speed,damage, on='NAME', how='inner')

    dps['DPS'] = dps.apply(lambda linha: linha.ATTACK_SPEED * linha.ATTACK_DAMAGE, axis=1)
    
    dps = dps[['NAME','DPS']].sort_values('DPS', ascending=0).reset_index(drop=True)
    dps.index += 1
    dps['POSITION'] = dps.index
    return dps[['POSITION','NAME', 'DPS']]

