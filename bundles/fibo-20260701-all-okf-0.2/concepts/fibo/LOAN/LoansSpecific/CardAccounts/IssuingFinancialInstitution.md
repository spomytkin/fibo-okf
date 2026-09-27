---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: issuing financial institution
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: issuer and financial services provider that issues payment cards or performs, facilitates, or supports issuing
      services including but not limited to issuing banks and issuing processors
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.pcisecuritystandards.org/pci_security/glossary
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: issuing bank
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Issuer.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Issuer
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/IssuingFinancialInstitution
sources:
- id: fibo-source-dece66f4c9
  resource: references/fibo/LOAN/LoansSpecific/CardAccounts.rdf
  sha256: dece66f4c9b1f239652e87cc348f748a4ba083249a57e8f2f3c688bfe30e2f19
  title: FIBO source LOAN/LoansSpecific/CardAccounts.rdf
title: issuing financial institution
type: Ontology Class
---

# issuing financial institution

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/IssuingFinancialInstitution>

## Definition

issuer and financial services provider that issues payment cards or performs, facilitates, or supports issuing services including but not limited to issuing banks and issuing processors

## Relationships

- **Subclass of**: [Issuer](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Issuer.md)
- **Subclass of**: [FinancialServiceProvider](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md)

## Annotations

- **label**: issuing financial institution
- **definition**: issuer and financial services provider that issues payment cards or performs, facilitates, or supports issuing services including but not limited to issuing banks and issuing processors
- **adaptedFrom**: https://www.pcisecuritystandards.org/pci_security/glossary
- **synonym**: issuing bank

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
