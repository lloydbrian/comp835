from __future__ import division
import itertools
import re
import hashlib

# a shingle in this code is a string with K-words
K = 4


def jaccard_set(s1, s2):
    " takes two sets and returns Jaccard coefficient"
    u = s1.union(s2)
    i = s1.intersection(s2)
    return len(i)/len(u)


def make_a_set_of_tokens(doc):
    """makes a set of K-tokens"""

    # replace non-alphanumeric char with a space, and then split
    tokens = re.sub("[^\w]", " ",  doc).split()

    sh = set()
    for i in range(len(tokens)-K):
        t = tokens[i]
        for x in tokens[i+1:i+K]:
            t += ' ' + x
        sh.add(t)
    return sh

if __name__ == '__main__':

    documents = ["COMP 815 (M1) - Information Security - Topics include general security principles and practices, network and system security, access control methodology, and cryptography. Students develop a basic cryptographic system based on sound mathematical principles, elaborate on its features and refine it, and experiment with various ways to attack it. Some programming required.",
      "COMP 860 (M1) - Data Visualization & Comm - Through hand-on experience with a leading data-visualization tool, the course introduces the concepts of data visualization to allow students to communicate and analyze data effectively using visual techniques.",
      "COMP 890 (M1) - Internship - The internship experience enhances the student's academic achievements with real-world, professional IT projects through placement at business, industry, and other sponsoring organizations. The student is expected to apply knowledge and skills acquired through other coursework in the major to address and solve new, authentic problems identified by the internship employer. Under the direction of a faculty advisor and workplace supervisor, the student is expected to contribute to the information technology products, processes, or services of the organization. May be repeated for a maximum of 6 credits. Permission required. Cr/F."]

    shingles = []
    # handle documents one by one
    # makes a list of sets which are compresized of a list of K words string
    for doc in documents:
        # makes a set of tokens
        # sh = set([' ', ..., ' '])
        sh = make_a_set_of_tokens(doc)
        print("sh = %s") %(sh)

        # hasing
        bucket = map(hash, sh)

        # print("bucket = %s") %(bucket)

        # shingles : list of sets (sh)
        shingles.append(set(bucket))

    #print("shingles=%s") %(shingles)

    combinations = list( itertools.combinations([x for x in range(len(shingles))], 2) )
    print("combinations=%s") %(combinations)

    # compare each pair in combinations tuple of shingles
    for c in combinations:
        i1 = c[0]
        i2 = c[1]
        jac = jaccard_set(shingles[i1], shingles[i2])
        print("%s : jaccard=%s") %(c,jac)
