---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: regional sovereignty
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: legal person that corresponds to an administrative division, administrative unit, administrative entity or country
      subdivision (or, sometimes, geopolitical division or subnational entity), that has the capacity to incur debt, issue
      contracts, and enter into relations with other similar entities
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: A country may be divided into provinces, which, in turn, are divided into counties, which, in turn, may be divided
      in whole or in part into municipalities; and so on.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/Locations/GeopoliticalEntity
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/hasSharedSovereigntyOver
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/RegionalGovernment
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/isRepresentedBy
  subclass_of:
  - concept: /concepts/fibo/BE/GovernmentEntities/GovernmentEntities/Polity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/Polity
resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/RegionalSovereignty
sources:
- id: fibo-source-5deab1a754
  resource: references/fibo/BE/GovernmentEntities/GovernmentEntities.rdf
  sha256: 5deab1a75487a8f7ff902b567d86099df6c1e24acc1a3a06d0351785ed1d30d3
  title: FIBO source BE/GovernmentEntities/GovernmentEntities.rdf
title: regional sovereignty
type: Ontology Class
---

# regional sovereignty

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/RegionalSovereignty>

## Definition

legal person that corresponds to an administrative division, administrative unit, administrative entity or country subdivision (or, sometimes, geopolitical division or subnational entity), that has the capacity to incur debt, issue contracts, and enter into relations with other similar entities

## Relationships

- **Subclass of**: [Polity](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities/Polity.md)

## Constraints

- **[hasSharedSovereigntyOver](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities/hasSharedSovereigntyOver.md)**: some values from of type [GeopoliticalEntity](<https://www.omg.org/spec/Commons/Locations/GeopoliticalEntity>)
- **[isRepresentedBy](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities/isRepresentedBy.md)**: some values from of type [RegionalGovernment](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities/RegionalGovernment.md)

## Annotations

- **label**: regional sovereignty
- **definition**: legal person that corresponds to an administrative division, administrative unit, administrative entity or country subdivision (or, sometimes, geopolitical division or subnational entity), that has the capacity to incur debt, issue contracts, and enter into relations with other similar entities
- **example**: A country may be divided into provinces, which, in turn, are divided into counties, which, in turn, may be divided in whole or in part into municipalities; and so on.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
