
import json

genders = [
    "mens", "men's", "womens", "women's", "unisex"
]

clothing_types = [
    "clothing", "fashion", "apparel", "formal wear",
    "sportswear", "luxury clothing"
]

store_types = [
    "store", "website"
]


bigCities = [
#   // USA
  "new york", "los angeles", "chicago", "houston", "san francisco",

#   // UK & Europe
  "london", "paris", "berlin", "madrid", "rome", "amsterdam",
  "vienna", "zurich", "stockholm",

#   // Canada
  "toronto", "vancouver", "montreal", "calgary",

#   // Asia
  "tokyo", "osaka", "seoul", "beijing", "shanghai", "shenzhen",
  "hong kong", "singapore", "bangkok", "kuala lumpur",
  "mumbai", "delhi", "bengaluru", "chennai", "hyderabad",

#   // Middle East
  "dubai", "abu dhabi", "doha", "riyadh",

#   // Australia
  "sydney", "melbourne", "brisbane", "perth",

#   // Africa
  "cairo", "johannesburg", "cape town", "nairobi",

#   // South America
  "sao paulo", "rio de janeiro", "buenos aires", "santiago"
]



queries = []

# for gender in genders:
#     for clothing in clothing_types:
#         for store in store_types:
#             for geo in provinces + cities:
#                 queries.append(
#                     f"{gender} {clothing} {store} in {geo}"
#                 )


for clothing in clothing_types:
    for store in store_types:
        for geo in bigCities:
            queries.append(
                f" {clothing} {store} in {geo}"
            )

print(json.dumps(queries, indent=2))

# size of queries
print(f"Total queries generated: {len(queries)}")

# for gender in genders:
#     for clothing in clothing_types:
#         for modifier in business_modifiers:
#             for geo in provinces + cities:
#                 queries.append(
#                     f"{modifier} {gender} {clothing} in {geo}"
#                 )
