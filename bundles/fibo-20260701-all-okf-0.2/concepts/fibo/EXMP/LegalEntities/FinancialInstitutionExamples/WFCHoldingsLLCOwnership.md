---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: WFC Holdings, LLC ownership
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: entity ownership context for WFC Holdings, LLC, a wholly-owned subsidiary of Wells Fargo & Company
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
  - concept: /concepts/fibo/EXMP/LegalEntities/FinancialInstitutionExamples/WFCHoldingsLLC-US-DE.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/hasOwnedEntity
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/FinancialInstitutionExamples/WFCHoldingsLLC-US-DE
  - concept: /concepts/fibo/EXMP/LegalEntities/FinancialInstitutionExamples/WellsFargoAndCompany-US-DE.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/hasOwningEntity
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/FinancialInstitutionExamples/WellsFargoAndCompany-US-DE
resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/FinancialInstitutionExamples/WFCHoldingsLLCOwnership
sources:
- id: fibo-source-6ff400fc7d
  resource: references/fibo/EXMP/LegalEntities/FinancialInstitutionExamples.rdf
  sha256: 6ff400fc7d0d754db2229aaf69c84fc1cd792e55a497f9e3299ad0a0c42433f7
  title: FIBO source EXMP/LegalEntities/FinancialInstitutionExamples.rdf
title: WFC Holdings, LLC ownership
type: Ontology Individual
---

# WFC Holdings, LLC ownership

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/FinancialInstitutionExamples/WFCHoldingsLLCOwnership>

## Definition

entity ownership context for WFC Holdings, LLC, a wholly-owned subsidiary of Wells Fargo & Company

## Relationships

- **Related to**: [WFCHoldingsLLC-US-DE](/concepts/fibo/EXMP/LegalEntities/FinancialInstitutionExamples/WFCHoldingsLLC-US-DE.md)
- **Related to**: [WellsFargoAndCompany-US-DE](/concepts/fibo/EXMP/LegalEntities/FinancialInstitutionExamples/WellsFargoAndCompany-US-DE.md)
- **Related to**: [GenerallyAcceptedAccountingPrinciples](/concepts/fibo/BE/LegalEntities/LEIEntities/GenerallyAcceptedAccountingPrinciples.md)

## Annotations

- **label**: WFC Holdings, LLC ownership
- **definition**: entity ownership context for WFC Holdings, LLC, a wholly-owned subsidiary of Wells Fargo & Company
- **hasOwnershipPercentage**: 100

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
