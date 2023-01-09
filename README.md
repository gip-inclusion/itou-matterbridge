# Matterbridge sur une PaaS comme Clever Cloud

L'objectif de ce dépôt est de déployer Matterbridge sur Clever Cloud.


## Matterbridge

### Ajouter une nouvelle passerelle

Tout se passe dans `matterbridge.toml`. [Lire la doc officielle](https://github.com/42wim/matterbridge/wiki/Gateway-config-%28basic%29).

:warning: Dans Slack, il faut inviter l'application « Matterbridge » au canal à configurer. Pour cela, ouvrez
l'application Matterbridge et cliquez sur « Ajouter cette application à un canal ». Il faut le faire AVANT d'avoir modifié
`matterbridge.toml`, sinon Matterbridge ne pourra pas trouver le canal lors du déploiement.

Si les canaux à connecter dans Mattermost et dans Slack portent exactement le même nom, vous pouvez modifier la section
`[[samechannelgateway]]`.

Sinon :

```
# Each gateway share the same key (`[[gateway]]`) but creates a new entry.
# Configuration is based on lines order: channel names under [[gateway.inout]] and placed right after will be connected.
[[gateway]]
    name="gateway-unique-name"
    enable=true

# Channel names are different. For each one, create a [[gateway.inout]] entry.

# First channel to connect to.
[[gateway.inout]]
    account="mattermost.betagouv"
    channel="tmp-celinems-test"

# Second channel to connect to.
[[gateway.inout]]
    account="slack.itou"
    channel="tmp-celinems-test55"
```

### Plateformes connectées

- Slack Itou
- Mattermost Beta

### Problèmes connus

Chaque déploiement casse le lien entre un message parent et ses réponses (_threads_ ou fils). Il faut donc espacer au maximum les déploiements ou les effectuer pendant une période de moindre activité.


## Doc dev
### Fonctionnement

Matterbridge étant un démon, il n'est pas possible de le lancer sur une instance Clever Cloud sans y adjoindre
un serveur web.
Le serveur web permet à la sonde de Clever de vérifier que notre service est disponible. Lorsqu'une requête GET est effectuée,
le serveur web demande le statut de Matterbridge à Supervisor. Si la réponse est positive, une 200 est renvoyée. Sinon, une 500 est renvoyée et le serveur web se suicide.
La sonde de Clever passe toutes les minutes.

### Lancer le projet en local

Récupérez les variables d'environnement dans Bitwarden (note « Matterbridge »).

```
touch .envrc
pip install -r requirements.txt
./dl_matterbridge.sh
# Prod server
uwsgi --http 127.0.0.1:8000 --master -p 4 -w wsgi:app
# Dev server
python app/main.py
```

