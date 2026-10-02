---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: state-chartered bank
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: commercial bank whose charter is approved by a state banking regulator
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.ffiec.gov/npw/Help/InstitutionTypes
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A state bank is defined as any bank, banking association, trust company, savings bank, industrial bank (or similar
      depository institution operating substantially in the same manner as an industrial bank), or other banking institution
      which is engaged in the business of receiving deposits other than trust funds, and in the US, is incorporated under
      the laws of any State or which is operating under the Code of Law for the District of Columbia, including any cooperative
      bank or other unincorporated bank the deposits of which were insured by the Federal Deposit Insurance Corporation on
      the day before the date of the enactment of the Financial Institutions Reform, Recovery, and Enforcement Act of 1989.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: State-chartered banks may or may not be members of the Federal Reserve System, but typically belong to the Federal
      Deposit Insurance Corporation, who may be their primary federal regulator for those that are not FRS members.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/CommercialBank.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/CommercialBank
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/USBank.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/USBank
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/StateCharteredBank
sources:
- id: fibo-source-d9bfee9a32
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
  sha256: d9bfee9a3294cc99a3ff7688e325d68a9cc2158ec209ffd10a9a8e411af37f33
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
title: state-chartered bank
type: Ontology Class
---

# state-chartered bank

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/StateCharteredBank>

## Definition

commercial bank whose charter is approved by a state banking regulator

## Relationships

- **Subclass of**: [CommercialBank](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/CommercialBank.md)
- **Subclass of**: [USBank](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/USBank.md)

## Annotations

- **label**: state-chartered bank
- **definition**: commercial bank whose charter is approved by a state banking regulator
- **adaptedFrom**: https://www.ffiec.gov/npw/Help/InstitutionTypes
- **explanatoryNote**: A state bank is defined as any bank, banking association, trust company, savings bank, industrial bank (or similar depository institution operating substantially in the same manner as an industrial bank), or other banking institution which is engaged in the business of receiving deposits other than trust funds, and in the US, is incorporated under the laws of any State or which is operating under the Code of Law for the District of Columbia, including any cooperative bank or other unincorporated bank the deposits of which were insured by the Federal Deposit Insurance Corporation on the day before the date of the enactment of the Financial Institutions Reform, Recovery, and Enforcement Act of 1989.
- **explanatoryNote**: State-chartered banks may or may not be members of the Federal Reserve System, but typically belong to the Federal Deposit Insurance Corporation, who may be their primary federal regulator for those that are not FRS members.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
