---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: LuxCSD S.A.
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Lux CSD legal entity
  - predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/hasLegalFormAbbreviation
    value: Societe Anonyme
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasLegalName
    value: LuxCSD S.A.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The European Central Bank (ECB) approved LuxCSD for its Securities Settlement System (SSS).
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/StockCorporation
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/ClearstreamBankingHeadquartersAddress.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/hasHeadquartersAddress
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/ClearstreamBankingHeadquartersAddress
  - concept: /concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/ClearstreamBankingLegalAddress.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/hasLegalAddress
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/ClearstreamBankingLegalAddress
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: http://www.luxcsd.com/luxcsd-en/
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/LuxCSDSA
sources:
- id: fibo-source-7fb80db6c9
  resource: references/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities.rdf
  sha256: 7fb80db6c9bf1521e4fd15a83716ed1dd7131e04cc3eab330d443c2f46cfa2aa
  title: FIBO source FBC/FunctionalEntities/CommercialRegistrationAuthorities.rdf
title: LuxCSD S.A.
type: Ontology Individual
---

# LuxCSD S.A.

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/LuxCSDSA>

## Definition

Lux CSD legal entity

## Relationships

- **Related to**: [ClearstreamBankingHeadquartersAddress](/concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/ClearstreamBankingHeadquartersAddress.md)
- **Related to**: [ClearstreamBankingLegalAddress](/concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/ClearstreamBankingLegalAddress.md)
- **See also**: [luxcsd-en](<http://www.luxcsd.com/luxcsd-en/>)

## Annotations

- **label**: LuxCSD S.A.
- **definition**: Lux CSD legal entity
- **hasLegalFormAbbreviation**: Societe Anonyme
- **hasLegalName**: LuxCSD S.A.
- **explanatoryNote**: The European Central Bank (ECB) approved LuxCSD for its Securities Settlement System (SSS).

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
