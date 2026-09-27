---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: investment firm
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: any legal person whose regular occupation or business is the provision of one or more investment services to third
      parties and/or the performance of one or more investment activities on a professional basis
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32004L0039&from=en#page=9
  disjoint_with:
  - concept: /concepts/fibo/FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities/CreditInstitution.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities/CreditInstitution
  - concept: /concepts/fibo/FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities/LocalFirm.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities/LocalFirm
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities/CreditInstitutionInvestmentFirm.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities/CreditInstitutionInvestmentFirm
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities/InvestmentFirm
sources:
- id: fibo-source-760f05a832
  resource: references/fibo/FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities.rdf
  sha256: 760f05a8322c75aaef31b7b35eefe1470b4bd58ea40a9be94100e8fe641fce43
  title: FIBO source FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities.rdf
title: investment firm
type: Ontology Class
---

# investment firm

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities/InvestmentFirm>

## Definition

any legal person whose regular occupation or business is the provision of one or more investment services to third parties and/or the performance of one or more investment activities on a professional basis

## Relationships

- **Subclass of**: [CreditInstitutionInvestmentFirm](/concepts/fibo/FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities/CreditInstitutionInvestmentFirm.md)

## Constraints

- **Disjoint with**: [CreditInstitution](/concepts/fibo/FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities/CreditInstitution.md)
- **Disjoint with**: [LocalFirm](/concepts/fibo/FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities/LocalFirm.md)

## Annotations

- **label**: investment firm
- **definition**: any legal person whose regular occupation or business is the provision of one or more investment services to third parties and/or the performance of one or more investment activities on a professional basis
- **adaptedFrom**: http://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32004L0039&from=en#page=9

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
