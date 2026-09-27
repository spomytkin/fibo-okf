---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: local firm
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: a firm dealing for its own account on markets in financial futures or options or other derivatives and on cash
      markets for the sole purpose of hedging positions on derivatives markets, or dealing for the accounts of other members
      of those markets and being guaranteed by clearing members of the same markets, where responsibility for ensuring the
      performance of contracts entered into by such a firm is assumed by clearing members of the same markets
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32013R0575&from=EN#page=18
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities/CreditInstitutionInvestmentFirm.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities/CreditInstitutionInvestmentFirm
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/BrokerageFirm.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/BrokerageFirm
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities/LocalFirm
sources:
- id: fibo-source-760f05a832
  resource: references/fibo/FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities.rdf
  sha256: 760f05a8322c75aaef31b7b35eefe1470b4bd58ea40a9be94100e8fe641fce43
  title: FIBO source FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities.rdf
title: local firm
type: Ontology Class
---

# local firm

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities/LocalFirm>

## Definition

a firm dealing for its own account on markets in financial futures or options or other derivatives and on cash markets for the sole purpose of hedging positions on derivatives markets, or dealing for the accounts of other members of those markets and being guaranteed by clearing members of the same markets, where responsibility for ensuring the performance of contracts entered into by such a firm is assumed by clearing members of the same markets

## Relationships

- **Subclass of**: [CreditInstitutionInvestmentFirm](/concepts/fibo/FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities/CreditInstitutionInvestmentFirm.md)
- **Subclass of**: [BrokerageFirm](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/BrokerageFirm.md)

## Annotations

- **label**: local firm
- **definition**: a firm dealing for its own account on markets in financial futures or options or other derivatives and on cash markets for the sole purpose of hedging positions on derivatives markets, or dealing for the accounts of other members of those markets and being guaranteed by clearing members of the same markets, where responsibility for ensuring the performance of contracts entered into by such a firm is assumed by clearing members of the same markets
- **adaptedFrom**: http://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32013R0575&from=EN#page=18

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
