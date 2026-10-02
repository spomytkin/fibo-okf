---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: interdealer quotation system
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: automated system for organizing and disseminating price quotes by brokers and dealer firms that facilitates electronic
      trading in securities
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: The National Association of Securities Dealers Automatic Quotation (Nasdaq), Nasdaq SmallCap Market, and the Over-The-Counter
      Bulletin Board (OTCBB) exchange platforms are integrated into one IQS. By using this integrated system, investors have
      access to a wide range of securities, ranging from large blue-chip companies to smaller micro-caps.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: IQS
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.investopedia.com/terms/i/interdealerquotationsystem.asp
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.iso20022.org/sites/default/files/2021-12/ISO10383_MIC_Release_2_0_Factsheet.pdf
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.lawinsider.com/dictionary/inter-dealer-quotation-system
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: An IQS ties the price quotations of a number of exchanges together into one platform. This allows investors to
      more easily access security price quotations that would otherwise need to be monitored on several separate exchanges.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In the United States, an IQS is an automated interdealer quotation system of a national securities association
      registered pursuant to section 15A(a) of the Exchange Act (15 U.S.C. 78o-3(a)).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: inter-dealer quotation system
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    value: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketCategoryClassifier-IDQS
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/Markets/Exchange.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/Exchange
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/InterdealerQuotationSystem
sources:
- id: fibo-source-c024989361
  resource: references/fibo/FBC/FunctionalEntities/Markets.rdf
  sha256: c0249893617f6c64fb6b454763bcddfb73748067a0ae183e40b432e03fde24bf
  title: FIBO source FBC/FunctionalEntities/Markets.rdf
title: interdealer quotation system
type: Ontology Class
---

# interdealer quotation system

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/InterdealerQuotationSystem>

## Definition

automated system for organizing and disseminating price quotes by brokers and dealer firms that facilitates electronic trading in securities

## Relationships

- **Subclass of**: [Exchange](/concepts/fibo/FBC/FunctionalEntities/Markets/Exchange.md)

## Constraints

- **[isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketCategoryClassifier-IDQS`

## Annotations

- **label**: interdealer quotation system
- **definition**: automated system for organizing and disseminating price quotes by brokers and dealer firms that facilitates electronic trading in securities
- **example**: The National Association of Securities Dealers Automatic Quotation (Nasdaq), Nasdaq SmallCap Market, and the Over-The-Counter Bulletin Board (OTCBB) exchange platforms are integrated into one IQS. By using this integrated system, investors have access to a wide range of securities, ranging from large blue-chip companies to smaller micro-caps.
- **abbreviation**: IQS
- **adaptedFrom**: https://www.investopedia.com/terms/i/interdealerquotationsystem.asp
- **adaptedFrom**: https://www.iso20022.org/sites/default/files/2021-12/ISO10383_MIC_Release_2_0_Factsheet.pdf
- **adaptedFrom**: https://www.lawinsider.com/dictionary/inter-dealer-quotation-system
- **explanatoryNote**: An IQS ties the price quotations of a number of exchanges together into one platform. This allows investors to more easily access security price quotations that would otherwise need to be monitored on several separate exchanges.
- **explanatoryNote**: In the United States, an IQS is an automated interdealer quotation system of a national securities association registered pursuant to section 15A(a) of the Exchange Act (15 U.S.C. 78o-3(a)).
- **synonym**: inter-dealer quotation system

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
