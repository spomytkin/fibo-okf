---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: board capacity
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: authority to act in a fiduciary capacity with respect to the organization, including but not limited to determining
      and executing corporate policy
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/isConferredOn
    value: N867c3a9f902a41b89a36f319cc9ddc25
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isConferredBy
    value: N9bdbc1e00b4a43408d89e71c76ddc4ec
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/CompanyLaw
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/RegulatoryAgencies/isGovernedBy
  subclass_of:
  - concept: /concepts/fibo/FND/Law/LegalCapacity/DelegatedLegalAuthority.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/DelegatedLegalAuthority
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/BoardCapacity
sources:
- id: fibo-source-27c89de7b6
  resource: references/fibo/BE/OwnershipAndControl/Executives.rdf
  sha256: 27c89de7b6ec909d26a0a73d1d2b7cbaadf425eb5e6a488f681cc3eba80f91ca
  title: FIBO source BE/OwnershipAndControl/Executives.rdf
title: board capacity
type: Ontology Class
---

# board capacity

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/BoardCapacity>

## Definition

authority to act in a fiduciary capacity with respect to the organization, including but not limited to determining and executing corporate policy

## Relationships

- **Subclass of**: [DelegatedLegalAuthority](/concepts/fibo/FND/Law/LegalCapacity/DelegatedLegalAuthority.md)

## Constraints

- **[isConferredOn](/concepts/fibo/FND/Law/LegalCapacity/isConferredOn.md)**: some values from value `N867c3a9f902a41b89a36f319cc9ddc25`
- **[isConferredBy](/concepts/fibo/FND/Relations/Relations/isConferredBy.md)**: some values from value `N9bdbc1e00b4a43408d89e71c76ddc4ec`
- **[isGovernedBy](<https://www.omg.org/spec/Commons/RegulatoryAgencies/isGovernedBy>)**: min qualified cardinality 0 of type [CompanyLaw](/concepts/fibo/BE/OwnershipAndControl/Executives/CompanyLaw.md)

## Annotations

- **label**: board capacity
- **definition**: authority to act in a fiduciary capacity with respect to the organization, including but not limited to determining and executing corporate policy

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
