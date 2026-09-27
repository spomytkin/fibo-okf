---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: DTCC Data Repository ownership
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: entity ownership context for the DTCC Data Repository, a wholly owned subsidiary of the Depository Trust & Clearing
      Corporation
  - datatype: http://www.w3.org/2001/XMLSchema#decimal
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/hasOwnershipPercentage
    value: '100'
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/DirectConsolidation
  related_to:
  - concept: /concepts/fibo/BE/LegalEntities/LEIEntities/GenerallyAcceptedAccountingPrinciples.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/isQualifiedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/GenerallyAcceptedAccountingPrinciples
  - concept: /concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/DTCC-US-DE.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/hasOwningEntity
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/DTCC-US-DE
  - concept: /concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/DTCCDataRepositoryLLC-US-NY.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/hasOwnedEntity
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/DTCCDataRepositoryLLC-US-NY
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/DTCCDataRepositoryOwnership
sources:
- id: fibo-source-7fb80db6c9
  resource: references/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities.rdf
  sha256: 7fb80db6c9bf1521e4fd15a83716ed1dd7131e04cc3eab330d443c2f46cfa2aa
  title: FIBO source FBC/FunctionalEntities/CommercialRegistrationAuthorities.rdf
title: DTCC Data Repository ownership
type: Ontology Individual
---

# DTCC Data Repository ownership

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/DTCCDataRepositoryOwnership>

## Definition

entity ownership context for the DTCC Data Repository, a wholly owned subsidiary of the Depository Trust & Clearing Corporation

## Relationships

- **Related to**: [DTCCDataRepositoryLLC-US-NY](/concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/DTCCDataRepositoryLLC-US-NY.md)
- **Related to**: [DTCC-US-DE](/concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/DTCC-US-DE.md)
- **Related to**: [GenerallyAcceptedAccountingPrinciples](/concepts/fibo/BE/LegalEntities/LEIEntities/GenerallyAcceptedAccountingPrinciples.md)

## Annotations

- **label**: DTCC Data Repository ownership
- **definition**: entity ownership context for the DTCC Data Repository, a wholly owned subsidiary of the Depository Trust & Clearing Corporation
- **hasOwnershipPercentage**: 100

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
