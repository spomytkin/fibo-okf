---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: zip code scheme
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: system used in the U.S. to facilitate the delivery of mail, consisting of a five- or nine-digit code Zone Improvement
      Plan (ZIP) printed directly after the address, the first five digits (initial code) indicating the state and post office
      or postal zone, the last four (expanded code) the box section or number, portion of a rural route, building, or other
      specific delivery location
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasMember
    value: N58ab8206887943809f445fa123d34e40
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://pe.usps.com/cpim/ftp/pubs/Pub28/pub28.pdf
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/CodesAndCodeSets/CodeSet
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Identifiers/IdentificationScheme
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/NorthAmerica/USPostalServiceAddresses/ZipCodeScheme
sources:
- id: fibo-source-e1b8af13cf
  resource: references/fibo/FND/Places/NorthAmerica/USPostalServiceAddresses.rdf
  sha256: e1b8af13cfbd56c65e428ff820890c7d7d5b5057af269667e5305e15ef80b1c6
  title: FIBO source FND/Places/NorthAmerica/USPostalServiceAddresses.rdf
title: zip code scheme
type: Ontology Class
---

# zip code scheme

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/NorthAmerica/USPostalServiceAddresses/ZipCodeScheme>

## Definition

system used in the U.S. to facilitate the delivery of mail, consisting of a five- or nine-digit code Zone Improvement Plan (ZIP) printed directly after the address, the first five digits (initial code) indicating the state and post office or postal zone, the last four (expanded code) the box section or number, portion of a rural route, building, or other specific delivery location

## Relationships

- **See also**: [pub28.pdf](<https://pe.usps.com/cpim/ftp/pubs/Pub28/pub28.pdf>)
- **Subclass of**: [CodeSet](<https://www.omg.org/spec/Commons/CodesAndCodeSets/CodeSet>)
- **Subclass of**: [IdentificationScheme](<https://www.omg.org/spec/Commons/Identifiers/IdentificationScheme>)

## Constraints

- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: some values from value `N58ab8206887943809f445fa123d34e40`

## Annotations

- **label**: zip code scheme
- **definition**: system used in the U.S. to facilitate the delivery of mail, consisting of a five- or nine-digit code Zone Improvement Plan (ZIP) printed directly after the address, the first five digits (initial code) indicating the state and post office or postal zone, the last four (expanded code) the box section or number, portion of a rural route, building, or other specific delivery location

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
