---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: partner
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: co-owner, member, and agent of a partnership whose participation level, including proportional liabilities and
      share in the profit / loss of the business is specified in a partnership agreement
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://www.omg.org/spec/Commons/Organizations/LegalPerson
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    value: N4c9efce995ff41319c3a82ffc9576f56
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    value: N9d3e86fe54d84d71beec90ed8d7f8e9e
  subclass_of:
  - concept: /concepts/fibo/BE/OwnershipAndControl/OwnershipParties/ConstitutionalOwner.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/ConstitutionalOwner
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Organizations/OrganizationMember
resource: https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/Partner
sources:
- id: fibo-source-d8e7bd00bc
  resource: references/fibo/BE/Partnerships/Partnerships.rdf
  sha256: d8e7bd00bcec02116a8ba944082e7c83bd17338e42c9b9925e2ef483b7e1cacf
  title: FIBO source BE/Partnerships/Partnerships.rdf
title: partner
type: Ontology Class
---

# partner

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/Partner>

## Definition

co-owner, member, and agent of a partnership whose participation level, including proportional liabilities and share in the profit / loss of the business is specified in a partnership agreement

## Relationships

- **Subclass of**: [ConstitutionalOwner](/concepts/fibo/BE/OwnershipAndControl/OwnershipParties/ConstitutionalOwner.md)
- **Subclass of**: [OrganizationMember](<https://www.omg.org/spec/Commons/Organizations/OrganizationMember>)

## Constraints

- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: exact qualified cardinality 1 of type [LegalPerson](<https://www.omg.org/spec/Commons/Organizations/LegalPerson>)
- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from value `N4c9efce995ff41319c3a82ffc9576f56`
- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from value `N9d3e86fe54d84d71beec90ed8d7f8e9e`

## Annotations

- **label**: partner
- **definition**: co-owner, member, and agent of a partnership whose participation level, including proportional liabilities and share in the profit / loss of the business is specified in a partnership agreement

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
