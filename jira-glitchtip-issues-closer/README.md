# Glitchtip <-> Jira integration checker

## Open Jira issues for Glitchtip events
```json:table
{
    "fields": [
        {
            "key": "issue_url",
            "label": "Jira"
        },
        {
            "key": "glitchtip_url",
            "label": "Glitchtip"
        },
        {
            "key": "diff",
            "label": "Days since last event"
        }
    ],
    "items": [
        {
            "issue_url": "https://issues.redhat.com/browse/CCXDEV-15035",
            "glitchtip_url": "https://glitchtip.devshift.net/ccx/issues/3519280",
            "diff": 21
        },
        {
            "issue_url": "https://issues.redhat.com/browse/CCXDEV-15030",
            "glitchtip_url": "https://glitchtip.devshift.net/ccx/issues/3513355",
            "diff": 9
        },
        {
            "issue_url": "https://issues.redhat.com/browse/CCXDEV-14963",
            "glitchtip_url": "https://glitchtip.devshift.net/ccx/issues/3425398",
            "diff": 10
        },
        {
            "issue_url": "https://issues.redhat.com/browse/CCXDEV-14962",
            "glitchtip_url": "https://glitchtip.devshift.net/ccx/issues/3425397",
            "diff": 10
        },
        {
            "issue_url": "https://issues.redhat.com/browse/CCXDEV-14911",
            "glitchtip_url": "https://glitchtip.devshift.net/ccx/issues/3490094",
            "diff": 13
        },
        {
            "issue_url": "https://issues.redhat.com/browse/CCXDEV-14870",
            "glitchtip_url": "https://glitchtip.devshift.net/ccx/issues/3487421",
            "diff": null
        },
        {
            "issue_url": "https://issues.redhat.com/browse/CCXDEV-14869",
            "glitchtip_url": "https://glitchtip.devshift.net/ccx/issues/3487420",
            "diff": null
        },
        {
            "issue_url": "https://issues.redhat.com/browse/CCXDEV-14587",
            "glitchtip_url": "https://glitchtip.devshift.net/ccx/issues/3168916",
            "diff": 12
        },
        {
            "issue_url": "https://issues.redhat.com/browse/CCXDEV-13083",
            "glitchtip_url": "https://glitchtip.devshift.net/ccx/issues/79211",
            "diff": 24
        }
    ],
    "filter": true
}
```

## Glitchtip events with no Jira issues
```json:table
{
    "fields": [
        {
            "key": "glitchtip_url",
            "label": "Glitchtip"
        },
        {
            "key": "diff",
            "label": "Days since last event"
        }
    ],
    "items": [
        {
            "glitchtip_url": "https://glitchtip.devshift.net/ccx/issues/240733",
            "diff": 0
        },
        {
            "glitchtip_url": "https://glitchtip.devshift.net/ccx/issues/3147294",
            "diff": 0
        },
        {
            "glitchtip_url": "https://glitchtip.devshift.net/ccx/issues/3146851",
            "diff": 0
        },
        {
            "glitchtip_url": "https://glitchtip.devshift.net/ccx/issues/3148406",
            "diff": 0
        },
        {
            "glitchtip_url": "https://glitchtip.devshift.net/ccx/issues/3231416",
            "diff": 0
        }
    ],
    "filter": true
}
```

