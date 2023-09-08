import random
from concurrent.futures import ThreadPoolExecutor as ThreadPool

#random.seed(0)

# generate many DNA samples, need to be large, otherwise there's no point of a concurrent program
dna_samples = ["".join(random.choices(["A", "C", "G", "T"], k=10000)) for i in range(1000)]

SEARCH_SEQUENCE = "AAH"

def search_dna_sequence(sequence, sample):
    """
    Search a DNA sample in a DNA sequence
    :return: True if the sequence was found, False otherwise
    """
    return sequence in sample

def thread_job(sample_index):
    """
    Each thread searches the sequence in a given sample
    """
    if search_dna_sequence(SEARCH_SEQUENCE, dna_samples[sample_index]):
        return "DNA sequence found in sample {}".format(sample_index)
    return "DNA sequence not found in sample {}".format(sample_index)

if __name__ == "__main__":

    thread_pool = ThreadPool(max_workers=10)

    futures = []

    with thread_pool:
        # execute thread job using submit or map
        # using submit:
        for i in range(len(dna_samples)):
            future = thread_pool.submit(thread_job, i)
            futures.append(future)
        
        # using map:
        # futures = thread_pool.map(thread_job, range(len(dna_samples)))

    # print results
    for future in futures:
        print(future.result())
