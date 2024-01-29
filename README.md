[HTML Player](https://scratch.mit.edu/projects/863871016) (by [Mario-098](https://scratch.mit.edu/users/Mario-098/))

> [!WARNING]
> Use of this tool may violate ScratchTeam's terms of use.

```python
pip install scratchclient
pip install keyboard
pip install requests
```

## .svprofile
version,,username,,password,,nolog,,debuglog,,projectid

`1,,hello,,world,,false,,true,,#######`

## CloudVariable
`☁__REQUEST` Request URL

> Please use ASCII Character Encode (256=3x85+1) Limit: 85

`☁__STATUS` Data transaction status

- 0 : Free
- 10 : Requesting
- 20 : Succefy (When this returns, be sure to change it to `0`)
- 30 : (Undefined)
- 40 : Error (When this returns, be sure to change it to `0`)

`☁__GET1` `☁__GET2` `☁__GET3` Document content [READ ONLY]

> It returns ASCII Character Encode (768=3x256) Limit: 256
