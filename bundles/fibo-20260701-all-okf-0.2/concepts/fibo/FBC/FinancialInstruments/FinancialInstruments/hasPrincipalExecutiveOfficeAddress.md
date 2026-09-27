---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has principal executive office address
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: relates an organization, specifically the issuer of a financial instrument, to its principal executive address,
      as required for issuance of that instrument
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Note that in most cases, the principal executive office address is also the headquarters address for a company.
  domain:
  - predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://www.omg.org/spec/Commons/Organizations/LegalPerson
  range:
  - concept: /concepts/fibo/FND/Places/Addresses/ConventionalStreetAddress.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/ConventionalStreetAddress
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/BE/LegalEntities/FormalBusinessOrganizations/hasRegisteredAddress.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/hasRegisteredAddress
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/hasPrincipalExecutiveOfficeAddress
sources:
- id: fibo-source-b40f618e3f
  resource: references/fibo/FBC/FinancialInstruments/FinancialInstruments.rdf
  sha256: b40f618e3feb2ca2bdd67c28d622728874d183b83fab1c57f77493cd81da088c
  title: FIBO source FBC/FinancialInstruments/FinancialInstruments.rdf
title: has principal executive office address
type: Ontology Property
---

# has principal executive office address

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/hasPrincipalExecutiveOfficeAddress>

## Definition

relates an organization, specifically the issuer of a financial instrument, to its principal executive address, as required for issuance of that instrument

## Relationships

- **Domain**: [LegalPerson](<https://www.omg.org/spec/Commons/Organizations/LegalPerson>)
- **Range**: [ConventionalStreetAddress](/concepts/fibo/FND/Places/Addresses/ConventionalStreetAddress.md)
- **Subproperty of**: [hasRegisteredAddress](/concepts/fibo/BE/LegalEntities/FormalBusinessOrganizations/hasRegisteredAddress.md)

## Annotations

- **label**: has principal executive office address
- **definition**: relates an organization, specifically the issuer of a financial instrument, to its principal executive address, as required for issuance of that instrument
- **explanatoryNote**: Note that in most cases, the principal executive office address is also the headquarters address for a company.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
