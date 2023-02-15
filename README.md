# Fil Plus Checker

Fil plus checker is a tool for retrieval data based on deal id.The retrieval logs will be stored at logs/<deal_id>.log

## How to use

```commandline
chmod 700 lite_node.sh
./lite_node.sh
```

In another terminal,

```shell
python main.py <deal_id>
```

check the log for progress

```shell
tail -f log/<deal_id>.log
```

Sample Output

```
lotus client retrieve --provider f02030031 --pieceCid baga6ea4seaqclgtbobbn5cqz7zylla7j3r4zbv52mg253vhe2vdyv5dl4ppwykq QmYiq3D8SY5863wKxFHaqXhjSeMNR264wqGyLuBa5rud3a 20230214-050552.file >> log/24730285.log

ERROR: offer error: retrieval query offer errored: failed to fetch piece to retrieve from: getting pieces for cid 
QmYiq3D8SY5863wKxFHaqXhjSeMNR264wqGyLuBa5rud3a: getting pieces containing block QmYiq3D8SY5863wKxFHaqXhjSeMNR264wqGyLuBa5rud3a: failed to lookup index for mh 12209a435396877fb5a139de09920909d7e467374b0a7302a10f637a5a711aa83195, err: datastore: key not found
```
