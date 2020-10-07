log = {
    1: 2,
    3: 4

}

def func(log_key):
    if not log.get(log_key):
        log[log_key] = []
    log[log_key].append(1234)

func('ass')
print(log)
func('ass')
print(log)
func('asshole')
print(log)