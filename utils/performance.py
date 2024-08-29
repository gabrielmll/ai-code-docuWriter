import time 

def timelapse(start_time):
    """ Print the time lapse """
    elapsed_time = time.time() - start_time
    
    print(f"Tempo decorrido: {elapsed_time:.2f} segundos")

    return f"{elapsed_time:.2f}"