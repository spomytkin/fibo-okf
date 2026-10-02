---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: mortgage-backed security
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: debt obligations that represent claims to the cash flows from pools of mortgage loans, most commonly on residential
      property
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: MBS
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of Financial Instruments (CFI code), Fourth
      edition, 2019-10-01.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Mortgage loans are purchased from banks, mortgage companies and other originators, and then assembled into pools
      by a governmental, quasigovernmental or private entity. The entity then issues securities that represent claims on the
      principal and interest payments made by borrowers on the loans in the pool, a process known as securitization.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/MBSIssuer
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isIssuedBy
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/WeightedAverageCoupon
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/hasWac
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/WeightedAverageRemainingTerm
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Classifiers/isCharacterizedBy
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/PoolBackedSecurities/PoolBackedSecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/PoolBackedSecurity
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/MortgageBackedSecurity
sources:
- id: fibo-source-4a5facbded
  resource: references/fibo/MD/DebtTemporal/DebtAnalytics.rdf
  sha256: 4a5facbdedf24373f412662d54858a7e9bb5e857cf4bc60543d124abfb92804a
  title: FIBO source MD/DebtTemporal/DebtAnalytics.rdf
- id: fibo-source-025d7e8955
  resource: references/fibo/SEC/Debt/MortgageBackedSecurities.rdf
  sha256: 025d7e89558a319cbd2b60f6a11ca228190a5137c59ed5b5bf34878c5f976f60
  title: FIBO source SEC/Debt/MortgageBackedSecurities.rdf
title: mortgage-backed security
type: Ontology Class
---

# mortgage-backed security

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/MortgageBackedSecurity>

## Definition

debt obligations that represent claims to the cash flows from pools of mortgage loans, most commonly on residential property

## Relationships

- **Subclass of**: [PoolBackedSecurity](/concepts/fibo/SEC/Debt/PoolBackedSecurities/PoolBackedSecurity.md)

## Constraints

- **[isIssuedBy](/concepts/fibo/FND/Relations/Relations/isIssuedBy.md)**: some values from of type [MBSIssuer](/concepts/fibo/SEC/Debt/MortgageBackedSecurities/MBSIssuer.md)
- **[hasWac](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/hasWac.md)**: some values from of type [WeightedAverageCoupon](/concepts/fibo/SEC/Debt/PoolBackedSecurities/WeightedAverageCoupon.md)
- **[isCharacterizedBy](<https://www.omg.org/spec/Commons/Classifiers/isCharacterizedBy>)**: some values from of type [WeightedAverageRemainingTerm](/concepts/fibo/SEC/Debt/PoolBackedSecurities/WeightedAverageRemainingTerm.md)

## Annotations

- **label** (en): mortgage-backed security
- **definition** (en): debt obligations that represent claims to the cash flows from pools of mortgage loans, most commonly on residential property
- **abbreviation** (en): MBS
- **adaptedFrom**: ISO 10962, Securities and related financial instruments - Classification of Financial Instruments (CFI code), Fourth edition, 2019-10-01.
- **explanatoryNote**: Mortgage loans are purchased from banks, mortgage companies and other originators, and then assembled into pools by a governmental, quasigovernmental or private entity. The entity then issues securities that represent claims on the principal and interest payments made by borrowers on the loans in the pool, a process known as securitization.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
