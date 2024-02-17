class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic_dom = {}
        # create the dict with the domains and visits
        for url in cpdomains:
            count, domain = url.split()
            count = int(count)
            subdomains = domain.split('.')
            for i in range(len(subdomains)):
                subdomain = '.'.join(subdomains[i:])
                dic_dom[subdomain] = dic_dom.get(subdomain, 0) + count

        result = [f"{count} {domain}" for domain, count in dic_dom.items()]
        return result
