---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: London Stock Exchange
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: London Stock Exchange functional entity, which is a global business and financial information services and news
      provider, a securities exchange, and the SEDOL code issuer and registration authority
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: LSE
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/Publisher
  - https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider
  - https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/NationalNumberingAgency
  - https://www.omg.org/spec/Commons/RegistrationAuthorities/RegistrationAuthority
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/LondonStockExchangePlc.md
    predicate: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/LondonStockExchangePlc
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: http://www.londonstockexchange.com/home/homepage.htm
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/LondonStockExchange
sources:
- id: fibo-source-7fb80db6c9
  resource: references/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities.rdf
  sha256: 7fb80db6c9bf1521e4fd15a83716ed1dd7131e04cc3eab330d443c2f46cfa2aa
  title: FIBO source FBC/FunctionalEntities/CommercialRegistrationAuthorities.rdf
- id: fibo-source-be76358ba2
  resource: references/fibo/SEC/Securities/SecuritiesIdentificationIndividuals.rdf
  sha256: be76358ba2a858eedd6bae77ca133882b7a1e2862cc351839d6b047eb2b024fa
  title: FIBO source SEC/Securities/SecuritiesIdentificationIndividuals.rdf
title: London Stock Exchange
type: Ontology Individual
---

# London Stock Exchange

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/LondonStockExchange>

## Definition

London Stock Exchange functional entity, which is a global business and financial information services and news provider, a securities exchange, and the SEDOL code issuer and registration authority

## Relationships

- **Related to**: [LondonStockExchangePlc](/concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/LondonStockExchangePlc.md)
- **See also**: [homepage.htm](<http://www.londonstockexchange.com/home/homepage.htm>)

## Annotations

- **label**: London Stock Exchange
- **definition**: London Stock Exchange functional entity, which is a global business and financial information services and news provider, a securities exchange, and the SEDOL code issuer and registration authority
- **abbreviation**: LSE

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
