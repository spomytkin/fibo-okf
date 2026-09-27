---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Refinitiv instrument code
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: proprietary code for financial instruments and indices owned, managed, and distributed by the London Stock Exchange
      Group's LSEG Financial Solutions (branded as Refinitiv)
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: 'A Refinitiv Instrument Code (RIC), previously known as the Reuters Instrument Code, is a proprietary identifier
      used by Refinitiv (now LSEG Financial Solutions) to represent financial instrument related data. The composition of
      a RIC is dependent on the type of instrument.


      - Instrument code : Can be based on the exchange ticker code, ISIN or local code, currency code, and so on

      - Period or time interval : Can be an expiry month code for example

      - Delimiter : Usually a full stop used to separate the instrument code from the exchange code or a = sign for money
      securities.

      - Source code : Usually a single or double alpha-character capital unique to an exchange


      An equity RIC has several components: the Equity RIC root is in upper case, brokerage characters in lower case (if applicable),
      and finally an exchange identifier. These codes facilitate information lookup across various financial networks. The
      concept of RICs traces back to the Quotron service, which Thomson Reuters acquired in the 1980s. The division was spun
      out as Refinitiv in 2018. Refinitiv was acquired by the London Stock Exchange Group in 2021, and the organization was
      rebranded as LSEG Financial Solutions in 2023, though the name of the code and certain other branded concepts were retained.'
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: RIC
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://community.developers.refinitiv.com/questions/28938/ric-code-understandingidentificaiton.html
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isIssuedBy
    value: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/MarketDataProviders/LSEGFinancialSolutionsAsMarketDataProvider
  - kind: has_value
    property: https://www.omg.org/spec/Commons/Designators/isDefinedIn
    value: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/RefinitivInstrumentCodeScheme
  - kind: has_value
    property: https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredBy
    value: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/MarketDataProviders/LSEGFinancialSolutionsAsMarketDataProvider
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIdentification/ProprietarySecurityIdentifier.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/ProprietarySecurityIdentifier
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/RefinitivInstrumentCode
sources:
- id: fibo-source-be76358ba2
  resource: references/fibo/SEC/Securities/SecuritiesIdentificationIndividuals.rdf
  sha256: be76358ba2a858eedd6bae77ca133882b7a1e2862cc351839d6b047eb2b024fa
  title: FIBO source SEC/Securities/SecuritiesIdentificationIndividuals.rdf
title: Refinitiv instrument code
type: Ontology Class
---

# Refinitiv instrument code

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/RefinitivInstrumentCode>

## Definition

proprietary code for financial instruments and indices owned, managed, and distributed by the London Stock Exchange Group's LSEG Financial Solutions (branded as Refinitiv)

## Relationships

- **Subclass of**: [ProprietarySecurityIdentifier](/concepts/fibo/SEC/Securities/SecuritiesIdentification/ProprietarySecurityIdentifier.md)

## Constraints

- **[isIssuedBy](/concepts/fibo/FND/Relations/Relations/isIssuedBy.md)**: has value value `https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/MarketDataProviders/LSEGFinancialSolutionsAsMarketDataProvider`
- **[isDefinedIn](<https://www.omg.org/spec/Commons/Designators/isDefinedIn>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/RefinitivInstrumentCodeScheme`
- **[isRegisteredBy](<https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredBy>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/MarketDataProviders/LSEGFinancialSolutionsAsMarketDataProvider`

## Annotations

- **label**: Refinitiv instrument code
- **definition**: proprietary code for financial instruments and indices owned, managed, and distributed by the London Stock Exchange Group's LSEG Financial Solutions (branded as Refinitiv)
- **note**: A Refinitiv Instrument Code (RIC), previously known as the Reuters Instrument Code, is a proprietary identifier used by Refinitiv (now LSEG Financial Solutions) to represent financial instrument related data. The composition of a RIC is dependent on the type of instrument.  - Instrument code : Can be based on the exchange ticker code, ISIN or local code, currency code, and so on - Period or time interval : Can be an expiry month code for example - Delimiter : Usually a full stop used to separate the instrument code from the exchange code or a = sign for money securities. - Source code : Usually a single or double alpha-character capital unique to an exchange  An equity RIC has several components: the Equity RIC root is in upper case, brokerage characters in lower case (if applicable), and finally an exchange identifier. These codes facilitate information lookup across various financial networks. The concept of RICs traces back to the Quotron service, which Thomson Reuters acquired in the 1980s. The division was spun out as Refinitiv in 2018. Refinitiv was acquired by the London Stock Exchange Group in 2021, and the organization was rebranded as LSEG Financial Solutions in 2023, though the name of the code and certain other branded concepts were retained.
- **abbreviation**: RIC
- **adaptedFrom**: https://community.developers.refinitiv.com/questions/28938/ric-code-understandingidentificaiton.html

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
