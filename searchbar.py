class SearchBar:
    
    def get_search_input(self, request):
        if request.method == "POST":
            product_searched = request.POST.get('search_query')
        return product_searched
        