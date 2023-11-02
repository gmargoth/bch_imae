# bch_imae

Este codigo descarga automaticante la series del IMAE de Honduras.

```python
username = 'YOUR_USERNAME'
password = 'YOUR_PASSWORD'
save_to = 'C:\\Users\\gabri\\Downloads\\Query\\'
session = login_SISEE(username, password, save_to)

global_only = False
downaload_IMAE_query(session, global_only)
session.quit()

```
