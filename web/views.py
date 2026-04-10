import heapq

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import AirportForm, RouteForm, SearchNodeForm, ShortestPathForm
from .models import Airport, Route


def index(request):
    return render(request, "web/index.html")


# ✅ Add Route
def add_route(request):
    form = RouteForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, "Route added successfully!")
        return redirect("web:index")  # redirect to index

    return render(request, "web/add_route.html", {"form": form})


# ✅ List Airports
def airport_list(request):
    airports = Airport.objects.all()
    return render(request, "web/airports/airport_list.html", {"airports": airports})


# ✅ Create Airport
def airport_create(request):
    form = AirportForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("web:airport_list")
    return render(request, "web/airports/airport_form.html", {"form": form})


# ✅ Update Airport
def airport_update(request, pk):
    airport = get_object_or_404(Airport, pk=pk)
    form = AirportForm(request.POST or None, instance=airport)
    if form.is_valid():
        form.save()
        return redirect("web:airport_list")
    return render(request, "web/airports/airport_form.html", {"form": form})


# ✅ Delete Airport
def airport_delete(request, pk):
    airport = get_object_or_404(Airport, pk=pk)
    if request.method == "POST":
        airport.delete()
        return redirect("web:airport_list")
    return render(request, "web/airports/airport_delete.html", {"airport": airport})


# ✅ 1. Find Nth Left or Right Node
def find_nth_node(request):
    result = None
    form = SearchNodeForm(request.POST or None)

    if form.is_valid():
        current = form.cleaned_data["start_airport"]  # ✅ object now
        direction = form.cleaned_data["direction"]
        n = form.cleaned_data["n"]

        for _ in range(n):
            route = Route.objects.filter(
                parent=current, position__iexact=direction
            ).first()

            if not route:
                result = "Not Found"
                break

            current = route.child

        if not result:
            result = current.code

    return render(request, "web/nth_node.html", {"form": form, "result": result})


# ✅ 2. Longest Duration Node
def longest_route(request):
    route = Route.objects.order_by("-duration").first()
    return render(request, "web/longest.html", {"route": route})


# ✅ 3. Shortest Path (Dijkstra)
def shortest_path(request):
    result = None
    form = ShortestPathForm(request.POST or None)

    if form.is_valid():
        start = form.cleaned_data["source"]  # ✅ object
        end = form.cleaned_data["destination"]  # ✅ object

        # Dijkstra
        distances = {airport.id: float("inf") for airport in Airport.objects.all()}
        distances[start.id] = 0

        pq = [(0, start.id)]

        while pq:
            current_distance, current_id = heapq.heappop(pq)

            if current_id == end.id:
                result = current_distance
                break

            routes = Route.objects.filter(parent_id=current_id)

            for route in routes:
                new_dist = current_distance + route.duration

                if new_dist < distances[route.child.id]:
                    distances[route.child.id] = new_dist
                    heapq.heappush(pq, (new_dist, route.child.id))

        # ✅ No path case
        if result is None:
            result = "No Path Found"

    return render(request, "web/shortest.html", {"form": form, "result": result})
