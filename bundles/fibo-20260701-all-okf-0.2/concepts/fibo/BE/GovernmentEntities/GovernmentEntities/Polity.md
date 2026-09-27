---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: polity
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: legal person that is a supranational entity, crown, state, or subordinate civil authority, such as a province,
      prefecture, county, municipality, city, or district representing the people of that entity
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/Locations/GeopoliticalEntity
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/hasSovereigntyOver
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/Government
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/isRepresentedBy
  subclass_of:
  - concept: /concepts/fibo/BE/GovernmentEntities/GovernmentEntities/GovernmentBody.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/GovernmentBody
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Organizations/LegalPerson
resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/Polity
sources:
- id: fibo-source-5deab1a754
  resource: references/fibo/BE/GovernmentEntities/GovernmentEntities.rdf
  sha256: 5deab1a75487a8f7ff902b567d86099df6c1e24acc1a3a06d0351785ed1d30d3
  title: FIBO source BE/GovernmentEntities/GovernmentEntities.rdf
title: polity
type: Ontology Class
---

# polity

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/Polity>

## Definition

legal person that is a supranational entity, crown, state, or subordinate civil authority, such as a province, prefecture, county, municipality, city, or district representing the people of that entity

## Relationships

- **Subclass of**: [GovernmentBody](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities/GovernmentBody.md)
- **Subclass of**: [LegalPerson](<https://www.omg.org/spec/Commons/Organizations/LegalPerson>)

## Constraints

- **[hasSovereigntyOver](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities/hasSovereigntyOver.md)**: some values from of type [GeopoliticalEntity](<https://www.omg.org/spec/Commons/Locations/GeopoliticalEntity>)
- **[isRepresentedBy](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities/isRepresentedBy.md)**: some values from of type [Government](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities/Government.md)

## Annotations

- **label**: polity
- **definition**: legal person that is a supranational entity, crown, state, or subordinate civil authority, such as a province, prefecture, county, municipality, city, or district representing the people of that entity

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
