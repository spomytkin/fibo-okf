---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: security
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: financial instrument that can be bought or sold
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: Securities Exchange Act of 1934, as amended 12 August 2012
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A security can be any note, stock, treasury stock, security future, security-based swap, bond, debenture,certificate
      of interest or participation in any profit-sharing agreement or in any oil, gas, or other mineral royalty or lease,
      any collateral-trust certificate, preorganization certificate or subscription, transferable share, investment contract,
      voting-trust certificate, certificate of deposit for a security, any put, call, straddle, option, or privilege on any
      security, certificate of deposit, or group or index of securities (including any interest therein or based on the value
      thereof), or any put, call, straddle, option, or privilege entered into on a national securities exchange relating to
      foreign currency, or in general, any instrument commonly known as a security, or any certificate of interest or participation
      in, temporary or interim certificate for, receipt for, or warrant or right to subscribe to or purchase, any of the foregoing;
      but shall not include currency or any note, draft, bill of exchange, or bankers' acceptance which has a maturity at
      the time of issuance of not exceeding nine months, exclusive of days of grace, or any renewal thereof the maturity of
      which is likewise limited.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In the U.S., the Supreme Court has adopted a flexible and liberal approach in determining what constitutes a security.
      In its famous decision of SEC v. W.J. Howey Co., 328 U.S. 293, 90 L.Ed. 1244, 66 S.Ct. 1100 (1946), the Court held that
      land sales contracts for citrus groves in Florida, coupled with warranty deeds for the land and a contract to service
      the land, were 'investment contracts' and thus securities. The Court stated that [a]n investment contract for purposes
      of the Securities Act means a contract, transaction or scheme whereby a person invests his money in a common enterprise
      and is led to expect profits solely from the efforts of the promoter or a third party. 66 S.Ct. at 1103. According to
      the Court, it is immaterial whether the shares in the enterprise are evidenced by formal certificates or by nominal
      interests in the physical assets employed in the enterprise. 66 S.Ct. at 1104.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Some securities may be traded over the counter, or through an exchange, or via some other trading venue such as
      an electronic trading platform.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Whether a contract or other economic right is a security essentially depends on whether the holder of the contract
      is acting as an investor who seeks financial benefits based on the work of a promoter or a third party.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/isLegallyRecordedIn
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/SecurityForm
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/isIssuedInForm
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/RegistrationAuthorities/RegistrationAuthority
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/isRegisteredWith
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrument
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Security
sources:
- id: fibo-source-b40f618e3f
  resource: references/fibo/FBC/FinancialInstruments/FinancialInstruments.rdf
  sha256: b40f618e3feb2ca2bdd67c28d622728874d183b83fab1c57f77493cd81da088c
  title: FIBO source FBC/FinancialInstruments/FinancialInstruments.rdf
- id: fibo-source-7b3088e831
  resource: references/fibo/SEC/Securities/SecuritiesIssuance.rdf
  sha256: 7b3088e8315beedb43222e345522bb546f87fbbd6850833103c9ba84ea1d7ac0
  title: FIBO source SEC/Securities/SecuritiesIssuance.rdf
title: security
type: Ontology Class
---

# security

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Security>

## Definition

financial instrument that can be bought or sold

## Relationships

- **Subclass of**: [FinancialInstrument](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrument.md)

## Constraints

- **[isLegallyRecordedIn](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/isLegallyRecordedIn.md)**: exact qualified cardinality 1 of type [Jurisdiction](<https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction>)
- **[isIssuedInForm](/concepts/fibo/SEC/Securities/SecuritiesIssuance/isIssuedInForm.md)**: min qualified cardinality 0 of type [SecurityForm](/concepts/fibo/SEC/Securities/SecuritiesIssuance/SecurityForm.md)
- **[isRegisteredWith](/concepts/fibo/SEC/Securities/SecuritiesIssuance/isRegisteredWith.md)**: min qualified cardinality 0 of type [RegistrationAuthority](<https://www.omg.org/spec/Commons/RegistrationAuthorities/RegistrationAuthority>)

## Annotations

- **label**: security
- **definition**: financial instrument that can be bought or sold
- **adaptedFrom**: Securities Exchange Act of 1934, as amended 12 August 2012
- **explanatoryNote**: A security can be any note, stock, treasury stock, security future, security-based swap, bond, debenture,certificate of interest or participation in any profit-sharing agreement or in any oil, gas, or other mineral royalty or lease, any collateral-trust certificate, preorganization certificate or subscription, transferable share, investment contract, voting-trust certificate, certificate of deposit for a security, any put, call, straddle, option, or privilege on any security, certificate of deposit, or group or index of securities (including any interest therein or based on the value thereof), or any put, call, straddle, option, or privilege entered into on a national securities exchange relating to foreign currency, or in general, any instrument commonly known as a security, or any certificate of interest or participation in, temporary or interim certificate for, receipt for, or warrant or right to subscribe to or purchase, any of the foregoing; but shall not include currency or any note, draft, bill of exchange, or bankers' acceptance which has a maturity at the time of issuance of not exceeding nine months, exclusive of days of grace, or any renewal thereof the maturity of which is likewise limited.
- **explanatoryNote**: In the U.S., the Supreme Court has adopted a flexible and liberal approach in determining what constitutes a security. In its famous decision of SEC v. W.J. Howey Co., 328 U.S. 293, 90 L.Ed. 1244, 66 S.Ct. 1100 (1946), the Court held that land sales contracts for citrus groves in Florida, coupled with warranty deeds for the land and a contract to service the land, were 'investment contracts' and thus securities. The Court stated that [a]n investment contract for purposes of the Securities Act means a contract, transaction or scheme whereby a person invests his money in a common enterprise and is led to expect profits solely from the efforts of the promoter or a third party. 66 S.Ct. at 1103. According to the Court, it is immaterial whether the shares in the enterprise are evidenced by formal certificates or by nominal interests in the physical assets employed in the enterprise. 66 S.Ct. at 1104.
- **explanatoryNote**: Some securities may be traded over the counter, or through an exchange, or via some other trading venue such as an electronic trading platform.
- **explanatoryNote**: Whether a contract or other economic right is a security essentially depends on whether the holder of the contract is acting as an investor who seeks financial benefits based on the work of a promoter or a third party.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
