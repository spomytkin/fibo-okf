---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Citicorp LLC ownership
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: entity ownership context for Citicorp LLC, a wholly owned subsidiary of Citigroup Inc.
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
  - concept: /concepts/fibo/EXMP/LegalEntities/FinancialInstitutionExamples/CiticorpLLC-US-DE.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/hasOwnedEntity
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/FinancialInstitutionExamples/CiticorpLLC-US-DE
  - concept: /concepts/fibo/EXMP/LegalEntities/FinancialInstitutionExamples/CitigroupInc-US-DE.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/hasOwningEntity
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/FinancialInstitutionExamples/CitigroupInc-US-DE
resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/FinancialInstitutionExamples/CiticorpLLCOwnership
sources:
- id: fibo-source-6ff400fc7d
  resource: references/fibo/EXMP/LegalEntities/FinancialInstitutionExamples.rdf
  sha256: 6ff400fc7d0d754db2229aaf69c84fc1cd792e55a497f9e3299ad0a0c42433f7
  title: FIBO source EXMP/LegalEntities/FinancialInstitutionExamples.rdf
title: Citicorp LLC ownership
type: Ontology Individual
---

# Citicorp LLC ownership

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/FinancialInstitutionExamples/CiticorpLLCOwnership>

## Definition

entity ownership context for Citicorp LLC, a wholly owned subsidiary of Citigroup Inc.

## Relationships

- **Related to**: [CiticorpLLC-US-DE](/concepts/fibo/EXMP/LegalEntities/FinancialInstitutionExamples/CiticorpLLC-US-DE.md)
- **Related to**: [CitigroupInc-US-DE](/concepts/fibo/EXMP/LegalEntities/FinancialInstitutionExamples/CitigroupInc-US-DE.md)
- **Related to**: [GenerallyAcceptedAccountingPrinciples](/concepts/fibo/BE/LegalEntities/LEIEntities/GenerallyAcceptedAccountingPrinciples.md)

## Annotations

- **label**: Citicorp LLC ownership
- **definition**: entity ownership context for Citicorp LLC, a wholly owned subsidiary of Citigroup Inc.
- **hasOwnershipPercentage**: 100

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
