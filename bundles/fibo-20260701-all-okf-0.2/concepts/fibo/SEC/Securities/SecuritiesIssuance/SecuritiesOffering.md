---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: securities offering
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: offering of a security (or securities) for sale
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: Barron's Dictionary of Finance and Investment Terms, Ninth Edition, 2014.
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.investopedia.com/
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: If the offering is public, then it can only be made after regulatory registration requirements have been met. The
      securities may be new or a secondary offering of a previously issued security, and may include stock, multiple classes
      of equity shares, municipal or other government bonds, and so forth. Offerings, especially to the investment public,
      are typically made by an investment banker, or syndicate of investment bankers.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceDocuments/FinalProspectus
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/finalStateDescribedIn
  - filler: http://www.w3.org/2001/XMLSchema#string
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/offerIssueSeries
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryPrice
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/hasOfferingPrice
  - filler: https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasGoverningJurisdiction
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/OfferingDocument
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/isEvidencedBy
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isIssuedBy
    value: Nb9bc9f1c6cfd48a59c9779be6f064093
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/SecurityUnderwriter
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/isUnderwrittenBy
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Security
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/ListedSecurityIdentifier
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ThirdPartyAgent
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/PartiesAndSituations/hasPartyRole
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/Offering.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/Offering
  - concept: /concepts/fibo/FND/Agreements/Agreements/Agreement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/Agreement
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/SecuritiesOffering
sources:
- id: fibo-source-fa20b53ed2
  resource: references/fibo/BP/SecuritiesIssuance/IssuanceProcess.rdf
  sha256: fa20b53ed283631237b4ff106a6a421d47c8e9bcb760277569287fb0cabdce1f
  title: FIBO source BP/SecuritiesIssuance/IssuanceProcess.rdf
- id: fibo-source-7b3088e831
  resource: references/fibo/SEC/Securities/SecuritiesIssuance.rdf
  sha256: 7b3088e8315beedb43222e345522bb546f87fbbd6850833103c9ba84ea1d7ac0
  title: FIBO source SEC/Securities/SecuritiesIssuance.rdf
title: securities offering
type: Ontology Class
---

# securities offering

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/SecuritiesOffering>

## Definition

offering of a security (or securities) for sale

## Relationships

- **Subclass of**: [Offering](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/Offering.md)
- **Subclass of**: [Agreement](/concepts/fibo/FND/Agreements/Agreements/Agreement.md)

## Constraints

- **[finalStateDescribedIn](/concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/finalStateDescribedIn.md)**: some values from of type [FinalProspectus](/concepts/fibo/BP/SecuritiesIssuance/IssuanceDocuments/FinalProspectus.md)
- **[offerIssueSeries](/concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/offerIssueSeries.md)**: some values from of type [string](<http://www.w3.org/2001/XMLSchema#string>)
- **[hasOfferingPrice](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/hasOfferingPrice.md)**: exact qualified cardinality 1 of type [MonetaryPrice](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryPrice.md)
- **[hasGoverningJurisdiction](/concepts/fibo/FND/Agreements/Contracts/hasGoverningJurisdiction.md)**: some values from of type [Jurisdiction](<https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction>)
- **[isEvidencedBy](/concepts/fibo/FND/Agreements/Contracts/isEvidencedBy.md)**: some values from of type [OfferingDocument](/concepts/fibo/SEC/Securities/SecuritiesIssuance/OfferingDocument.md)
- **[isIssuedBy](/concepts/fibo/FND/Relations/Relations/isIssuedBy.md)**: some values from value `Nb9bc9f1c6cfd48a59c9779be6f064093`
- **[isUnderwrittenBy](/concepts/fibo/SEC/Securities/SecuritiesIssuance/isUnderwrittenBy.md)**: min qualified cardinality 0 of type [SecurityUnderwriter](/concepts/fibo/SEC/Securities/SecuritiesIssuance/SecurityUnderwriter.md)
- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: some values from of type [Security](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Security.md)
- **[isIdentifiedBy](<https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy>)**: some values from of type [ListedSecurityIdentifier](/concepts/fibo/SEC/Securities/SecuritiesIdentification/ListedSecurityIdentifier.md)
- **[hasPartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/hasPartyRole>)**: min qualified cardinality 0 of type [ThirdPartyAgent](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/ThirdPartyAgent.md)

## Annotations

- **label**: securities offering
- **definition**: offering of a security (or securities) for sale
- **adaptedFrom**: Barron's Dictionary of Finance and Investment Terms, Ninth Edition, 2014.
- **adaptedFrom**: http://www.investopedia.com/
- **explanatoryNote**: If the offering is public, then it can only be made after regulatory registration requirements have been met. The securities may be new or a secondary offering of a previously issued security, and may include stock, multiple classes of equity shares, municipal or other government bonds, and so forth. Offerings, especially to the investment public, are typically made by an investment banker, or syndicate of investment bankers.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
